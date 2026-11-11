#!/usr/bin/env python3
"""Gera uma página Markdown completa (com Mermaid incluso) + graph.json
a partir dos RFs e do mapa de fluxo de usuários.

Entradas:
  - rfs.yaml            : lista de RFs (id, nome, descricao, entrega.*, priorizacao.*)
  - fluxo_usuarios.yaml : mapa das conexões entre RFs (fonte da verdade do fluxo)

Saídas (por padrão em docs/generated/):
  - fluxo_usuarios.md   : página completa pronta pro MkDocs, com Mermaid incluso
  - graph.json          : grafo estruturado consumido pelo plugin Figma

Uso:
  python gerar_fluxo.py [--rfs rfs.yaml] [--fluxo fluxo_usuarios.yaml] [--out docs/generated]

Formato esperado de fluxo_usuarios.yaml:

  caminhos:
    - id: conta-e-acesso
      passos: [RF01, RF02]          # sequência linear
  ramificacoes:                     # opcional: transições condicionais/exceções
    - de: RF01
      para: RF01e
      rotulo: "Dados a corrigir"
"""

import argparse
import hashlib
import json
import sys
from pathlib import Path

import yaml


# ---------------------------------------------------------------- utils

def die(msg: str) -> None:
    print(f"[erro] {msg}", file=sys.stderr)
    sys.exit(1)


def load_yaml(path: Path):
    try:
        with path.open(encoding="utf-8") as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        die(f"arquivo não encontrado: {path}")
    except yaml.YAMLError as e:
        die(f"YAML inválido em {path}: {e}")


def sanitize_id(rf_id: str) -> str:
    return "".join(ch if ch.isalnum() or ch == "_" else "_" for ch in rf_id)


def esc(s: str) -> str:
    return s.replace('"', '\\"').replace("\n", " ")


# ---------------------------------------------------------------- validações

def validar(rfs, fluxo):
    if not isinstance(rfs, list) or not rfs:
        die("rfs.yaml deve ser uma lista de RFs não vazia")

    index: dict[str, dict] = {}
    for rf in rfs:
        rid = rf.get("id")
        if not rid:
            die(f"RF sem 'id': {rf.get('nome', '(sem nome)')}")
        if rid in index:
            die(f"id duplicado: {rid}")
        for campo in ("nome", "descricao"):
            if not rf.get(campo):
                die(f"{rid}: campo obrigatório ausente '{campo}'")
        if not rf.get("entrega", {}).get("jornada"):
            die(f"{rid}: 'entrega.jornada' ausente (usado para agrupar o fluxo)")
        index[rid] = rf

    nodos_validos = set(index)
    arestas: list[tuple[str, str, str]] = []

    for caminho in fluxo.get("caminhos") or []:
        passos = caminho.get("passos") or []
        if len(passos) < 2:
            print(f"[aviso] caminho '{caminho.get('id')}' com menos de 2 passos, "
                  f"ignorado", file=sys.stderr)
            continue
        for origem, destino in zip(passos, passos[1:]):
            for passo in (origem, destino):
                if passo not in nodos_validos and not any(
                        p == passo for _, p, _ in arestas
                ) and not any(d == passo for d, _, _ in arestas):
                    print(f"[aviso] passo '{passo}' não existe nos RFs — "
                          f"tratado como nó auxiliar do fluxo", file=sys.stderr)
            arestas.append((origem, destino, ""))

    for ram in fluxo.get("ramificacoes") or []:
        arestas.append((ram["de"], ram["para"], ram.get("rotulo", "")))

    # grafo conexo (apenas aviso)
    adj: dict[str, list[str]] = {}
    for de, para, _ in arestas:
        adj.setdefault(de, []).append(para)
        adj.setdefault(para, []).append(de)
    if arestas:
        visitados, fila = set(), [next(iter(adj))]
        while fila:
            n = fila.pop()
            if n in visitados:
                continue
            visitados.add(n)
            fila.extend(m for m in adj.get(n, []) if m not in visitados)
        fora = set(adj) - visitados
        if fora:
            print(f"[aviso] nós fora do grafo principal: {sorted(fora)}",
                  file=sys.stderr)

    return index, arestas


# ---------------------------------------------------------------- mermaid

def gerar_mermaid(index, arestas) -> str:
    jornadas: dict[str, list[str]] = {}
    auxiliares: set[str] = set()
    for de, para, _ in arestas:
        for n in (de, para):
            if n in index:
                jornadas.setdefault(index[n]["entrega"]["jornada"], []).append(n)
            else:
                auxiliares.add(n)

    linhas = ["flowchart TD"]

    for jornada, rids in jornadas.items():
        primeiro = index[rids[0]]
        label = jornada
        escopo = primeiro.get("entrega", {}).get("escopo")
        it = primeiro.get("entrega", {}).get("iteracao")
        if escopo:
            label += f" ({escopo}"
            if it is not None:
                label += f", iteração {it}"
            label += ")"
        sub_id = "J_" + sanitize_id(jornada.replace(" ", "_"))
        linhas.append(f'    subgraph {sub_id}["{esc(label)}"]')
        for rid in sorted(set(rids)):
            linhas.append(f'        {sanitize_id(rid)}'
                          f'["{esc(rid)} — {esc(index[rid]["nome"])}"]')
        linhas.append("    end")

    if auxiliares:
        linhas.append('    subgraph J_aux["Exceções e estados auxiliares"]')
        for n in sorted(auxiliares):
            linhas.append(f'        {sanitize_id(n)}["{esc(n)}"]')
        linhas.append("    end")

    linhas.append("")
    for de, para, rotulo in arestas:
        if rotulo:
            linhas.append(f'    {sanitize_id(de)} -->|"{esc(rotulo)}"'
                          f'| {sanitize_id(para)}')
        else:
            linhas.append(f"    {sanitize_id(de)} --> {sanitize_id(para)}")

    return "\n".join(linhas)


# ---------------------------------------------------------------- markdown

def cabecalho_indexado(index) -> dict[int, str]:
    """Mapeia posição no YAML -> id, para preservar a ordem original dos RFs."""
    return {i: rid for i, rid in enumerate(index)}


def gerar_markdown(index, arestas, mermaid: str, origem_header=None) -> str:
    def chips(rf: dict) -> str:
        entrega = rf.get("entrega", {})
        prio = rf.get("priorizacao", {})
        partes = []
        if entrega.get("escopo"):
            partes.append(f"`{entrega['escopo']}`")
        if entrega.get("iteracao") is not None:
            partes.append(f"`iteração {entrega['iteracao']}`")
        if prio.get("moscow"):
            partes.append(f"**{prio['moscow']}**")
        if rf.get("origem"):
            partes.append("origem: " + ", ".join(map(str, rf["origem"])))
        return " · ".join(partes)

    linhas = [
        "# Fluxo de usuários",
        "",
        "> **Página gerada automaticamente** a partir de `rfs.yaml` e "
        "`fluxo_usuarios.yaml` pelo script `gerar_fluxo.py`. **Não editar diretamente** — "
        "altere a fonte e rode o script (o CI faz isso no build).",
        "",
        "O diagrama abaixo representa as funcionalidades do sistema como uma máquina "
        "de estados de alto nível: cada nó é um requisito funcional, cada seta é uma "
        "transição de responsabilidade entre usuário e sistema.",
        "",
    ]

    jornadas: dict[str, list[str]] = {}
    auxiliares: set[str] = set()
    for de, para, _ in arestas:
        for n in (de, para):
            if n in index:
                jornadas.setdefault(index[n]["entrega"]["jornada"], []).append(n)
            else:
                auxiliares.add(n)

    # sumário das jornadas
    linhas.append("## Jornadas")
    linhas.append("")
    for jornada, rids in jornadas.items():
        anc = jornada.lower().replace(" ", "-")
        qtd = len(set(rids))
        linhas.append(f"- [{jornada}](#{anc}) — {qtd} requisito"
                      f"{'s' if qtd != 1 else ''}")
    linhas.append("")

    linhas.append("## Diagrama")
    linhas.append("")
    linhas.append("```mermaid")
    linhas.append(mermaid)
    linhas.append("```")
    linhas.append("")

    # legenda de nós auxiliares
    if auxiliares:
        linhas.append("**Nós auxiliares** (não correspondem a um RF; representam "
                      "estados de exceção do fluxo): "
                      + ", ".join(f"`{n}`" for n in sorted(auxiliares)))
        linhas.append("")

    # seções por jornada, RFs na ordem original do YAML
    for jornada in jornadas:
        linhas.append(f"## {jornada}")
        linhas.append("")
        for rid in (r for r in index if index[r]["entrega"]["jornada"] == jornada
                    and r in set(jornadas[jornada])):
            rf = index[rid]
            linhas.append(f"### {rid} — {rf['nome']}")
            linhas.append("")
            linhas.append(rf["descricao"])
            meta = chips(rf)
            if meta:
                linhas.append("")
                linhas.append(meta)
            # transições deste nó
            saidas = [(p, rt) for d, p, rt in arestas if d == rid]
            entradas = [(d, rt) for d, p, rt in arestas if p == rid]
            if saidas or entradas:
                linhas.append("")
                if entradas:
                    txt = "; ".join(
                        f"{d}{' — ' + rt if rt else ''}" for d, rt in entradas)
                    linhas.append(f"**Recebe de:** {txt}")
                if saidas:
                    txt = "; ".join(
                        f"{p}{' — ' + rt if rt else ''}" for p, rt in saidas)
                    linhas.append(f"**Leva a:** {txt}")
            linhas.append("")

    return "\n".join(linhas) + "\n"


# ---------------------------------------------------------------- graph.json

def gerar_graph_json(index, arestas) -> dict:
    nodos = []
    for rid, rf in index.items():
        entrega = rf.get("entrega", {})
        nodos.append({
            "id": rid,
            "nome": rf["nome"],
            "descricao": rf["descricao"],
            "jornada": entrega.get("jornada"),
            "escopo": entrega.get("escopo"),
            "iteracao": entrega.get("iteracao"),
            "moscow": rf.get("priorizacao", {}).get("moscow"),
            "origem": rf.get("origem", []),
        })
    ids_nos_rfs = set(index)
    vistos = set(ids_nos_rfs)
    for de, para, _ in arestas:
        for n in (de, para):
            if n not in vistos:
                vistos.add(n)
                nodos.append({"id": n, "nome": n, "descricao": "",
                              "auxiliar": True})
    rels = sorted(
        ({"de": de, "para": para, "rotulo": rotulo} for de, para, rotulo in arestas),
        key=lambda r: (r["de"], r["para"], r["rotulo"]),
    )
    return {"nodes": nodos, "edges": rels}


# ---------------------------------------------------------------- main

def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--rfs", default="rfs.yaml", type=Path)
    ap.add_argument("--fluxo", default="fluxo_usuarios.yaml", type=Path)
    ap.add_argument("--out", default="docs/generated", type=Path)
    ap.add_argument("--titulo", default="Fluxo de usuários",
                    help="Título H1 da página gerada")
    args = ap.parse_args()

    rfs = load_yaml(args.rfs)
    fluxo = load_yaml(args.fluxo) or {}

    index, arestas = validar(rfs, fluxo)

    mermaid = gerar_mermaid(index, arestas)
    md = gerar_markdown(index, arestas, mermaid)
    graph = gerar_graph_json(index, arestas)
    graph["_hash"] = hashlib.sha256(
        json.dumps(graph, sort_keys=True).encode()).hexdigest()

    args.out.mkdir(parents=True, exist_ok=True)
    (args.out / "fluxo_usuarios.md").write_text(md, encoding="utf-8")
    (args.out / "graph.json").write_text(
        json.dumps(graph, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"OK: {len(index)} RFs, {len(arestas)} arestas -> "
          f"{args.out}/fluxo_usuarios.md, {args.out}/graph.json")


if __name__ == "__main__":
    main()
