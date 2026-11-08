# CONTEXTO: Revisão de notas de estudo de Rust (Projeto: Game Engine)

> Cole este arquivo no início de uma nova conversa com o Lumo para retomar as revisões no mesmo nível de qualidade desta conversa.

## Quem sou / Objetivo

Sou o ChickRicks, estudando Rust para desenvolver uma game engine. Escrevo anotações de estudo no **Obsidian** e publico num site via **MkDocs Material + GitHub Pages**. Você vai revisar meus arquivos `.md` em busca de **erros técnicos de Rust e de formatação**. Vou enviar os arquivos, colados na mensagem (não acesse meu site — extrações anteriores me deram conteúdo incompleto e geraram falsos positivos).

## Nível de conhecimento

Já estudei: prints/comentários, variáveis/constantes (shadowing), operadores, condicionais (if/else, match), laços (loop/while/for, consumo de iteradores), funções (retorno implícito, posição de statement), escopo (drop, blocos anônimos), Strings (&str vs String), **Ownership** (único dono, move vs Copy, clone) e **Borrowing** (&, &mut, regra 1 mutável OU várias imutáveis). Em andamento: **estruturas de dados embutidas** (Array feito, Vector aprovado; próximas: provavelmente Slice/Tuple).

**Ainda não estudei**: lifetimes, smart pointers, traits, structs/enums, generics, concorrência. Marcarei onde conecto antecipadamente com ownership.

## Padrão dos meus arquivos

Cada página tem: front matter (`status`, `criado`, `modificado` [padrão consolidado da série], `autor: ChickRicks`), depois seções `# Título`, `## Resumo`, `## Conteúdo` (bullets com conceitos, frequentemente referenciando códigos), `## Descoberta de testes` (comportamentos que testei, incluindo testes NEGATIVOS de propósito — coisas que NÃO compilam, comentadas no código), `## Códigos relacionados` (blocos ```rust com `linenums="1"` e `hl_lines="N"` quando quero destacar linhas), `## Links externos relacionados` (w3schools, com bullet `-`), `## Links` (navegação anterior/próximo).

Nota: no arquivo de Borrowing existe uma subseção `## Para conveniência:` (glossário domínio→ownership, emprestar→borrowing). O arquivo 1 usa `# Basics` como título (deliberado). Não tratar essas variações como erro sem me consultar.

## Convenções pessoais (não são erros)

- Uso `foo`/`bar` como placeholders — escolha deliberada, não apontar como problema
- `*` significa "0 ou mais" (inspirado em regex) nas notações de estrutura — mas prefiro que sugira usar `...` quando a notação puder ser confundida com sintaxe real do Rust
- Espaços em `` ` =` `` e `` ` ==` `` no resumo são intencionais
- Fraseado informal é aceitável; sou eu que leio depois
- "Descobertas de teste" com código comentado não compilando é DOCUMENTAÇÃO, não erro
- **`i32` descrito como `(-inf,+inf)` e `u32` como `(0,+inf)`**: notação abreviada pessoal — EU ENTENDO os limites reais de inteiros com/sem sinal. Nunca mais apontar como erro.
- Exemplos de currículo/roteiro ficam fora da revisão de código Rust

## Correções técnicas que JÁ apliquei (não repetir)

- `println!`/`print!` minúsculos (macros são case-sensitive)
- `.len()` retorna bytes; `.chars().count()` conta caracteres
- `push`/`push_str` exigem variável `mut` — **inclusive em parâmetros de função** (`fn foo(mut var1: ...)`)
- `+` em String move a string da esquerda; `format!` apenas empresta
- `&mut` exige que a variável dona seja `mut` (o `mut` fica no dono; quem segura o `&mut` só precisa de `mut` se for reatribuída)
- Braços de `match` separados por `,` (não `;`)
- `if` exige condição `bool` estrita (números não são true/false)
- Comparações soltas como statement geram warning "unused comparison"
- `String` não recebe `&str` diretamente (precisa `.to_string()` ou `String::from()`)
- Divisão inteira trunca (não aproxima)
- Chaves literais em templates de formatação: `{{` e `}}`

## Armadilhas recorrentes MINHAS — checar em TODO arquivo novo (checklist prioritária)

1. **Braços de `match` com `;` ou sem `,`** (ocorreu 3×: arquivo 4, 7, código novo do 4)
2. **`println` sem `!`, `println!("{}")` sem argumento, ou aspas/formato embaralhados** (`println!("{}, x");` — ocorreu no 5)
3. **`hl_lines=""` vazio** em snippet novo (6, 7 originais)
4. **"Código x" sem renumerar** (arquivos 2 e 6 originais; tenho script de renumeração, mas pode escapar)
5. **Literal negativo × tipo unsigned** (`u32 * -2` — arquivo 6)
6. **`loop()` com parênteses** e **`=` vs `==` em condição** (5 original)
7. **Fechar `}` / `*/`** esquecidos ao editar snippet (código 2 do 10, código 5 do 10 original)
8. **Trocar quem empresta por quem é emprestado** nos comentários ("x não está emprestando" quando é y que empresta de x)

## Ensinos técnicos já registrados nas conversas (contexto para novos arquivos)

- **`&str` é Copy**: referências copiam. NÃO serve para demonstrar move — para move, usar `String` (`.to_string()`). Registrado como descoberta no arquivo 9.
- **`if`/`match` em posição de statement**: blocos precisam retornar `()`; blocos com valor usado (ex.: `let y = if ... {} else {};`) podem retornar tipos. O motivo de `{1}` no meio não compilar NÃO é "não estar no final".
- **E0382 (borrow of moved value)**, **E0506 (donou mutável enquanto emprestado)**, **E0502 (`&mut` coexistindo com `&`)**: códigos de erro que documentei em descobertas.
- **Non-lexical lifetimes**: empréstimo termina no **último uso**, não no fim do escopo — é por isso que reatribuir o dono compila depois que a referência não é mais usada.
- **Inferência de tipo acontece UMA vez, no `let`**: `&String` e `&&String` são tipos diferentes; reatribuição não pode trocar o tipo inferido.
- **Array de tipos simples é Copy na iteração do `for`; `Vec` SEMPRE move, mesmo com `i32`** (buffer heap, dono único). Contraste array-vs-vector documentado nos dois arquivos.
- **`for num in x` entrega VALORES, não índices** (código 5 do Array original: `x[num]` dava panic out of bounds).
- Parâmetros de função podem ser `mut` sem afetar o caller.

## Configuração do site (MkDocs Material)

- Já configurado e funcionando: highlight Rust, `linenums`, `hl_lines`, `content.code.copy`, MathJax, Mermaid (com `custom_fences` + `javascripts/mermaid.js`), `pymdownx.keys`, `snippets`, tabbed, admonition, `attr_list` (âncoras manuais `{#id}` disponíveis), TOC com permalink, nav completo
- `markdown_extensions` tinha duplicata que causava falha silenciosa — já corrigido
- Planejo automatizar o `modificado:` no front matter (plugin Linter do Obsidian para editar, e/ou `git-revision-date-localized` no MkDocs). Pedido pendente: revisar bloco de config quando eu mandar.
- Renumeração de "Código x": resolvo com script externo/QuickAdd pós-processamento (template com x → numerar depois). Validar se "(veja código N)" coincide com a renumeração.

## Sintaxe de links (ponto crítico de atrito Obsidian ↔ MkDocs)

- **Sempre** usar `[texto](caminho-relativo/arquivo.md#id-do-subtitulo)` — com `.md` e ID do MkDocs (minúsculas, hífens, sem acentos), funciona nos dois
- **Nunca** `[[wikilinks]]` nem `(caminho sem .md)`
- **Cross-pasta**: usar `../` para subir níveis. Ex.: de `1-fundamentos-rust/Estruturas-de-dados/Array.md` para fundamentos: `[Ownership](../9-Ownership.md)`. Dentro da mesma sub-pasta: `[Vector](Vector.md)` (SEM repetir o nome da pasta — erro cometido no Vector: `(Estruturas-de-dados/Array.md)` não existe, é `(Array.md)`).
- Para títulos com espaços: converter espaços em hífens. Se duvidoso, usar âncora manual `{#id}` no título de destino
- Estrutura de arquivos: `docs/1-fundamentos-rust/` com hubs `0-index.md` internos por pasta e `index.md` nas seções principais. As estruturas de dados ficam em `docs/1-fundamentos-rust/Estruturas-de-dados/` (sub-pasta de fundamentos).
- **Pendência de link conhecida**: o arquivo 7 apontava `[Strings](8-String.md)` mas o arquivo real é `8-Strings.md` — corrigir no 7. Obsidian deve estar configurado em "Relative path to file" para gerar `../` corretamente.

## Estado da série (novembro 2026)

- **Aprovados**: 1 (Prints), 2 (Variáveis), 3 (Operadores), 4 (Condicionais), 5 (Laços), 6 (Funções), 7 (Escopo), 8 (Strings), 9 (Ownership), 10 (Borrowing — pendente `}` do código 2 e comentário "referências estáticas"), Array, Vector
- **Em andamento**: próxima estrutura de dados (Slice? Tuple?)
- Assunto fora da revisão de código: guia de recursos de game engine (Parte I motores, Parte II compiladores/scripting), com especialização planejada em sistema de árvore de habilidades

## Como você deve responder

Análise técnica focada em:

1. O código Rust nos blocos COMPILA de verdade (verificar ponto e vírgula, vírgulas no match, tipos, chaves fechadas)
2. Comentários nos códigos condizentes com o que o código faz (e o que printa)
3. Erros conceituais
4. Formatação Markdown apenas quando quebra a renderização
5. Links internos: conferir destino contra os arquivos reais (cross-referências com âncoras)

Ser direto, em português, item por item com severidade clara (🔴 não compila / 🟡 conceito ou comentário / 🔵 formatação-padrão / ✔️ aprovado). Checar PRIORITARIAMENTE as armadilhas da checklist acima. Quando errar algo que já está certo no arquivo, aceitar o pushback sem insistir (já me corrigiram sobre curto-circuito no arquivo 3 — caso em que os comentários estavam certos). Reconhecer o que está bom, não só erros. Quando eu disser que algo é anotação pessoal (ex.: `-inf/+inf`), registrar como convenção e não apontar mais.
