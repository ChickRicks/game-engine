---
status: Em andamento
criado: 2026-11-01
modificado: 2026-11-01
autor: ChickRicks
---
# Funções

## Resumo
Estrutura completa: `fn foo(foo1) -> bar{bar}`. `return` para as funções que retornam algo.

## Conteúdo
- Função possui estrutura `fn foo(foo1) -> bar{bar}`, todos sendo necessários.
- Para funções que recebem mais de um valor, fica `fn foo(foo1: bar1, foo2: bar2){}`.
- Chamar uma função é `foo()`.
- O conteúdo de variáveis da função envolve `foo: tipo de var`.
- Para funções que retornam valores, usa-se `-> tipo de var` na criação. Todas retornam algo, caso não possua, retorna ()
- Para o retorno de funções, pode se usar `return` ou, na última linha, fazer a operação sem `;`.
- Pode passar ownership para as variáveis complexas caso não seja usado `&` com a variável.

## Descoberta de testes
- Não sei se parece bom usar `fn` que retorna valor sem `return`, fica confuso.
- É exclusivo do fim de linha o retorno implícito.

## Links externos relacionados
[w3school funcitons](https://www.w3schools.com/rust/rust_functions.php)
## Links
- 👈 **Anterior:** [Lastros de Repetição](5-Lacos-de-repeticao.md)
- ➡️ **Próximo:** [Escopo](7-Escopo.md)
