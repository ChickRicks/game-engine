---
status: Em andamento
criado: 2026/11/01
atualizado: 2026/11/01
autor: ChickRicks
---

# Condicionais

## Resumo
Estrutura do ifs, if_else, else if e match
if (completo): `if foo {bar} else if foo2 {bar2} else {bar3}`.
match: `match foo { foo1 => bar1,* _ => bar2}`.
## Conteúdo
- ifs possuem estrutura: `if foo {foo} (else if {foo})* else {foo}`.
- Ifs também podem ser usados como "função" de uma variável, porém, em caso de if else, eles devem retornar o mesmo valor
- Match possui estrutura `match foo { foo => bar,*  _ => bar}`, sendo _ valor caso não esteja dentro dos outros.
- Match aceita uso de | caso alguns valores devam retornar o mesmo resultado.
- Similar ao if, também pode ser uma "função", com as mesmas regras do if (os valores que retornam tem que ser do mesmo tipo).
-  Para borrowing e Ownership: o bloco interno do `if` pode trocar o ownership de variáveis de escopos externos.
## Descoberta de testes
- `If` aceita apenas valores booleanos, números não tem tradução de true ou false.
## Links externos relacionados
-  [w3school if.else](https://www.w3schools.com/rust/rust_if_else.php) e [w3school match](https://www.w3schools.com/rust/rust_match.php).
## Links
- 👈 **Anterior:** [Operadores](3-Operadores.md)
- ➡️ **Próximo:** [Lastro de Repetição](5-Lacos-de-repeticao.md)

