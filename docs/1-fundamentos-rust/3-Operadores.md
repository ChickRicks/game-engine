---
status: Em andamento
criado: 2026/11/01
atualizado: 2026/11/01
autor: ChickRicks
---

# Operadores

## Resumo
 Operadores válidos: `+`, `-`, `/`, `*`, `%`, ` =`, `+=`, `-=`, `*=`, `/=`, `%=` ` ==`, `!=`, `>`, `<`, `>=`, `<=`, `&&`, `||`,`!`.

## Conteúdo
- Operadores aritméticos:
	- `+` : Soma (`foo + foo2`);
	- `-` : Subtração (`foo - foo2`);
	- `*` : Multiplicação (`foo * foo2`);
	- `/` : Divisão (`foo / foo2`);
	- `%` : Resto da divisão/módulo (`foo%foo2`);
- Operadores definidores de variável:
	- ` = ` : Move o valor da direita a esquerda em casos de variáveis complexas, ou copia em caso de variáveis simples (`foo = bar`);
	- `+=` : Some o valor da esquerda ao da direita, e depois salva o valor (`foo += bar` = `foo = foo + bar`);
	- `-=` : Subtraia o valor da esquerda ao da direita, e depois salva o valor (`foo -= bar` = `foo = foo - bar`);
	- `*=` : Multiplique o valor da esquerda ao da direita, e depois salva o valor (`foo *= bar` = ` foo = foo * bar`);
	- `/=` : Divida o valor da esquerda ao da direita, e depois salva o valor (`foo /= foo` = `foo = foo/bar`);
	- `%=` : Faça o módulo da esquerda ao da direita, e depois salva o valor (`foo %= foo` = `foo = foo % bar`);
- Operadores Comparadores:
	-  ` == ` : Igualdade entre os 2 (`foo == foo`);
	- `!=` : Diferenças entre os 2 (`foo != foo`);
	- `>` : Esquerda é maior que a direita (`foo > foo`);
	- `<` : Esquerda é menor que a direita (`foo < foo`);
	- `>=` : Esquerda é maior ou igual que a direita (`foo >= foo`);
	- `<=` : Esquerda é menor ou igual que a direita (`foo <= foo`);
- Operadores Lógicos:
	- `&&` -> E lógico (`foo && foo`);
	- `||` -> OU lógico (`foo || foo`);
	- `!` -> NÃO lógico (`!foo`);
- Se a parte esquerda de `&&` for falsa, ela retorna falso, sem avaliação da direita.
- Se a parte esquerda de `||` for verdadeira, ela retorna verdadeiro, sem avaliação da direita.
- Ao criar variáveis, ela pode receber uma "função" para resolver, e receber o resultado dela. Ex: `let x = 10; let y = x * 7`.

## Descoberta de testes
- Divisão inteira não aproxima, retorna o valor cheio.
## Links externos relacionados
- [w3schools operators](https://www.w3schools.com/rust/rust_operators.php) e [w3schools booleans](https://www.w3schools.com/rust/rust_booleans.php).

##Links
- 👈 **Anterior:** [Variáveis e Constantes](2-Variaveis-e-constantes.md)
- ➡️ **Próximo:** [Condicionais](4-Condicionais.md)

---
