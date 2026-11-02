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
- Montada planejada para manter o uso de memória segura.
- Um valor possui um único dono
- Quando o dono sai de escopo, ele é removido da memória
- [Existem formas de "emprestar" o valor](10-Borrowing.md#conteudo), mas em geral só existe um dono do valor
- Variáveis complexas trocam de dono, variáveis simples copiam seu valor para frente.
- `.clone()` pode ser usado para copiar valores para outra variável, sem trocar o dono do valor.

## Descoberta de testes

## Links externos relacionados

## Links
- 👈 **Anterior:** [Strings](8-Strings.md)
- ➡️ **Próximo:** [Borrowing](10-Borrowing.md)
