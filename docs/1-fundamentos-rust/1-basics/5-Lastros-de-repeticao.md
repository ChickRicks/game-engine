---
status: pendente
criado: "2026-11-01"
modificado: "2026-11-01"
autor: ChickRicks
---
# Lastros de repetição

## Resumo
Possuem 3:
	`loop{}` : loop infinito, parado apenas com break ou parando o código
	`While(foo){}` : loop acontece enquanto a condição estiver correta
	`for foo in foo..foo{}` : loop dentro de um alcance definido
`break` : para a função loop em questão
`continue` : pula para a próxima iteração do loop

## Conteúdo
- Existem 3 estruturas de lastro de repetição: loop, while e for.
- `loop{bar}` faz um loop infinito, sem nenhuma limitação de parar.
- Um `break` faz com que a função de lastro de repetição pare sua condição.
- Caso não coloque uma condição de parada dentro com um `break`, ele precisa ser parado com ctrl + c.
- `loop{bar}` pode ser usado como uma "função" de variável, usando o break como um return.
- `while(foo) {bar}` faz o loop até a condição ser falsa.
- Caso a condição seja inicialmente falsa, ele não começa.
- Além da condição ser falsa, também pode ser parada por um break.
- `continue` faz com que o resto do while seja ignorado, mas continua funcionando
- `for foo in foo1..foo2{bar}` cria um lastro com restrições.
- `foo2` é o limite, sem estar incluso.
- Para `foo2` ser incluso, deve ser `for foo in foo1..=foo2{bar}`.
- A variável incremental (`foo`) aumenta sozinha com +1 naturalmente.
- `break` e `continue` funcionam normalmente para o `for`.
## Descoberta de testes
-  Possui prioridade linear (o que está acima acontece antes do que está abaixo). Breaks barram o que ia acontecer depois.
- `continue` não traz aumento de condicional do while.
- No `for`, `foo1` e `foo2` podem ser variáveis criadas anteriormente.
- `foo1` e `foo2` do `for` é válido usar caracteres, e ele vai da letra inicial até a letra final (entre maiúculas para maiúsculas ou entre minúsculas para minúsculas, sem mistura).
- `for` não é uma boa ideia se o incremento não for +1.

## Links externos relacionados

- De [w3school loops](https://www.w3schools.com/rust/rust_loops.php) Até [w3school for loops](https://www.w3schools.com/rust/rust_loops_for.php)

## Links
- 👈 **Anterior:** [Condicionais](4-Condicionais.md)
- ➡️ **Próximo:** [Funções](6-Funcoes)