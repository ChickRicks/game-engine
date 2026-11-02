---
status: Em andamento
criado: 2026/10/31
atualizado: 2026/11/01
autor: ChickRicks
---
# Basics

## Resumo

`println!(foo)` para print com quebra de linha, `print!(foo)` para prints sem a quebra, `//` para comentários de uma linha, `/* comentário */` para comentários de mais de uma linha.
## Conteúdo

- `println!("Conteúdo");` : print com quebra de linha.
- `print!("Conteúdo");` : print sem quebra de linha.
- Mais de um print possível, incluindo intercalado.
- Não serão ignorados espaços brancos dentro da palavra chave, mas dentro de conteúdo de string funciona (`Cont\neúdo` funciona, e ele considera o texto com uma quebra de linha).
- Ter uma "!" dentro de print! e println! demonstram ser macros.
- String do rust entende carácteres funcionais (\n para quebra de linha, \0 para vazio, etc).
- Comentários de linha única tem "//".
- Comentários de muitas linhas tem '/ * ' de começo e ' \*/' no final.
## Descobertas de teste
- `Print!\n("Conteúdo");` funciona normalmente (espaços branco ignorados).
- Parênteses obrigatórios (`println!(Conteúdo);` funciona, `println!Conteúdo;` não).
## Links externos relacionados
- [w3schools síntaxe](https://www.w3schools.com/rust/rust_syntax.php) até [w3schools comments](https://www.w3schools.com/rust/rust_comments.php ).

## Links
- 👈 **Anterior:** [index](0-index.md)
- ➡️ **Próximo:** [Variaveis e Constantes](2-Variaveis-e-constantes.md)
---
