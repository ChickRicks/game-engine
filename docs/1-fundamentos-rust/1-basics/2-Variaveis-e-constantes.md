
---
status: Em andamento
criado: 2026/11/01
atualizado: 2026/11/01
autor: ChickRicks
---
# Variaveis e constantes

## Resumo

Estrutura de Variáveis e constantes.
Variável não modificável: `let foo = bar;`
Variável modificável: `let mut foo = bar;`
Constante: `const foo1: foo2 = bar;`, sendo foo2 o tipo da constante.

## Conteúdo
-  Declaração de variável: `let foo = bar;`
-  Para chamar a variável em uma string (para um print, por exemplo), usa-se "{}"
- Naturalmente, `let foo = bar;` criam variáveis que não mudam.
- Para variáveis que podem mudar facilmente, monta-se `let mut foo = bar;`
- Rust aceita inteiros, pontos flutuantes, caracteres, booleana, strings, entre outras estruturas.
- Tem como deixar explícito o chamado de tipo de variável usando: `let foo: foo = bar;`.
- Tipos de variável:
	- i32: Números inteiros (-inf,+inf);
	- u32: Números naturais + 0 (0,+inf);
	- f64: números de ponto flutuante;
	- char: um carácter único;
	- &str: uma string;
	- bool: booleana (V ou F);
- Print aceita os dados mostrados
- Constantes possuem estrutura `const foo: foo2 = bar;`, sendo que foo2 é o tipo de variável
- A estrutura é obrigatória incluir o tipo da constante.
- Ideal usar letras maiúsculas para constantes, facilitam a diferenciação.

## Descoberta de testes
-  Quebras de linha nos espaços continuam ignorados (dado que não corte palavras chaves ou valores).
- `let x = foo; -> let x = foo2;` é válido.
## Links relacionados
- https://www.w3schools.com/rust/rust_variables.php até https://www.w3schools.com/rust/rust_constants.php
---
