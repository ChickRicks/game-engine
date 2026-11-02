---
status: Em andamento
criado: 2026-11-02
modificado: 2026-11-02
autor: ChickRicks
---
# Borrowing

## Resumo
Pode-se passar a referência de valor de um dono para outra variável sem passar transferência usando `&`, que também precisa de um `mut` próprio para ser mutável.
## Para conveniência:
Ao usar domínio, traduza para ownership.
## Conteúdo
- Referenciar é olhar o valor sem transferir o domínio.
- Caso queira passar o conteúdo para outra variável sem passar o domínio, pode-se usar o símbolo `&` para isso.
- Para referências serem mutáveis, elas também tem que ter o `mut` próprio
- Reduz a quantidade de `clones()`, tornando o código mais rápido.
- O valor dono precisa ser mutável para que o valor copiado seja.
- Podem existir múltiplas referências imutáveis, porém 1 única referência mutável, e nenhum pode acontecer ao mesmo tempo.

## Descoberta de testes

## Links externos relacionados
[w3school Borrowing](https://www.w3schools.com/rust/rust_borrowing_references.php)

## Links
- 👈 **Anterior:** [Ownership](9-Ownership.md)
- ➡️ **Próximo:** [XXX](XXX)
