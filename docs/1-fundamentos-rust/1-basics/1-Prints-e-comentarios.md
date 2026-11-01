
---
status: Em andamento
criado: 2026/10/31
atualizado: 2026/11/01
autor: ChickRicks
---
# Basics

## Resumo

Formato de print e comentários, nenhum comando técnico muito aprofundado, com inclusão de testes aleatórios.
## Conteúdo

- `Println!("Conteúdo");` : print com quebra de linha.
- `Print!("Conteúdo");` : print sem quebra de linha.
- Parênteses obrigatórios (`println!(Conteúdo);` funciona, `println!Conteúdo;` não).
- Mais de um print possível, incluindo intercalado.
- `Print!\n("Conteúdo");` funciona normalmente (espaços branco ignorados).
- Não serão ignorados espaços brancos dentro da palavra chave, mas dentro de conteúdo de string funciona (`Cont\neúdo` funciona, e ele considera o texto com uma quebra de linha).
- Ter uma "!" dentro de print! e println! demonstram ser macros.
- String do rust entende carácteres funcionais (\n para quebra de linha, \0 para vazio, etc).
- Comentários de linha única tem "//".
- Comentários de muitas linhas tem '/ * ' de começo e ' * /' no final.
## Links relacionados
- [w3schools síntaxe](https://www.w3schools.com/rust/rust_syntax.php) até [w3schools commets](https://www.w3schools.com/rust/rust_comments.php ).
---
