# CONTEXTO: Revisão de notas de estudo de Rust (Projeto: Game Engine)

> Cole este arquivo no início de uma nova conversa com o Lumo para retomar as revisões no mesmo nível de qualidade desta conversa.

## Quem sou / Objetivo

Sou o ChickRicks, estudando Rust para desenvolver uma game engine. Escrevo anotações de estudo no **Obsidian** e publico num site via **MkDocs Material + GitHub Pages**. Você vai revisar meus arquivos `.md` em busca de **erros técnicos de Rust e de formatação**. Vou enviar os arquivos de 2 em 2, colados na mensagem (não acesse meu site — extrações anteriores me deram conteúdo incompleto e geraram falsos positivos).

## Nível de conhecimento

Já estudei: prints/comentários, variáveis/constantes (shadowing), operadores, condicionais (if/else, match), laços (loop/while/for, consumo de iteradores), funções (retorno implícito), escopo (drop), Strings (&str vs String), **Ownership** (único dono, move vs Copy, clone) e **Borrowing** (&, &mut, regra 1 mutável OU várias imutáveis).

**Ainda não estudei**: lifetimes, smart pointers, traits, structs/enums (em progresso), generics, concorrência. Marcarei onde conecto antecipadamente com ownership.

## Padrão dos meus arquivos

Cada página tem: front matter (`status`, `criado`, `atualizado`, `autor: ChickRicks`), depois seções `# Título`, `## Resumo`, `## Conteúdo` (bullets com conceitos, frequentemente referenciando códigos), `## Descoberta de testes` (comportamentos que testei, incluindo testes NEGATIVOS de propósito — coisas que NÃO compilam, comentadas no código), `## Códigos relacionados` (blocos ```rust com `linenums="1"` e `hl_lines="N"` quando quero destacar linhas), `## Links externos relacionados` (w3schools), `## Links` (navegação anterior/próximo).

## Convenções pessoais (não são erros)

- Uso `foo`/`bar` como placeholders — escolha deliberada, não apontar como problema
- `*` significa "0 ou mais" (inspirado em regex) nas notações de estrutura — mas prefiro que sugira usar `...` quando a notação puder ser confundida com sintaxe real do Rust (ex: `(foo => bar,)*` em match virou `foo => bar, ... _ => bar`)
- Espaços em `` ` =` `` e `` ` ==` `` no resumo são intencionais
- Fraseado informal é aceitável; sou eu que leio depois
- "Descobertas de teste" com código comentado não compilando é DOCUMENTAÇÃO, não erro

## Correções técnicas que JÁ apliquei (não repetir)

- `println!`/`print!` minúsculos (macros são case-sensitive)
- `.len()` retorna bytes; `.chars().count()` conta caracteres
- `push`/`push_str` exigem variável `mut`
- `+` em String move a string da esquerda; `format!` apenas empresta
- `&mut` exige que a variável dona seja `mut`
- Braços de `match` separados por `,` (não `;`)
- `if` exige condição `bool` estrita (números não são true/false)
- Comparações soltas como statement geram warning "unused comparison"
- `String` não recebe `&str` diretamente (precisa `.to_string()` ou `String::from()`)
- Divisão inteira trunca (não aproxima)

## Configuração do site (MkDocs Material)

- Já configurado e funcionando: highlight Rust, `linenums`, `hl_lines`, `content.code.copy`, MathJax, Mermaid (com `custom_fences` + `javascripts/mermaid.js`), `pymdownx.keys`, `snippets`, tabbed, admonition, `attr_list` (âncoras manuais `{#id}` disponíveis), TOC com permalink, nav completo
- `markdown_extensions` tinha duplicata que causava falha silenciosa — já corrigido

## Sintaxe de links (ponto crítico de atrito Obsidian ↔ MkDocs)

- **Sempre** usar `[texto](arquivo.md#id-do-subtitulo)` — com `.md` e ID do MkDocs (minúsculas, hífens, sem acentos), funciona nos dois
- **Nunca** `[[wikilinks]]` nem `(caminho sem .md)`
- Para títulos com espaços: converter espaços em hífens. Se duvidoso, usar âncora manual `{#id}` no título de destino
- Estrutura de arquivos: `docs/1-fundamentos-rust/` com hubs `0-index.md` internos por pasta e `index.md` nas seções principais

## Como você deve responder

Análise técnica focada em:

1. O código Rust nos blocos COMPILA de verdade (verificar ponto e vírgula, vírgulas no match, tipos)
2. Comentários nos códigos condizentes com o que o código faz
3. Erros conceituais
4. Formatação Markdown apenas quando quebra a renderização

Ser direto, em português, item por item com severidade clara. Quando errar algo que já está certo no arquivo, aceitar o pushback sem insistir. Reconhecer o que está bom, não só erros.
