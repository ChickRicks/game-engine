---
status: Em andamento
criado: 2026-11-02
modificado: 2026-11-02
autor: ChickRicks
---
# Ownership

## Resumo
Em geral, um valor possui apenas um dono, exceto se ela for emprestada.

## Conteúdo
- Montada planejada para manter o uso de memória segura, sem uso de garbage collector de memória.
- Um valor possui um único dono.
- Quando o dono sai de escopo, ele é removido da memória.
- [Existem formas de "emprestar" o valor](10-Borrowing.md#conteudo), mas em geral só existe um dono do valor.
- Variáveis complexas trocam de dono, variáveis simples copiam seu valor para frente.
	- Variáveis simples: i32,bool,char;
	- Variáveis complexas: String, Vec;
- `.clone()` pode ser usado para copiar valores para outra variável, sem trocar o dono do valor.

## Descoberta de testes

## Links externos relacionados
- [w3school Ownership](https://www.w3schools.com/rust/rust_ownership.php)

## Links
- 👈 **Anterior:** [Strings](8-Strings.md)
- ➡️ **Próximo:** [Borrowing](10-Borrowing.md)
