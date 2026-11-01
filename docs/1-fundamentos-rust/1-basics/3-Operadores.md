
---
status: Em andamento
criado: 2026/11/01
atualizado: 2026/11/01
autor: ChickRicks
---

# Operadores

## Resumo
 Operadores válidos:
	 +
	 -
	 /
	 *
	 %
	 =
	 +=
	 -=
	 \*=
	 /=
	 %=
	 \==
	 !=
	 \>
	 <
	 \>=
	 <=
	 &&
	 ||
	 !

## Conteúdo
- Operadores aritméticos:
	- `+` : Soma (`foo + foo2`);
	- `-` : Subtração (`foo - foo2`);
	- `*` : Multiplicação (`foo * foo2`);
	- `/` : Divisão (`foo / foo2`);
	- `%` : Resto da divisão/módulo (`foo%foo2`);
- Operadores definidores de variável:
	- ` = ` : Coloque o valor da direita a esquerda (`foo = bar`);
	- `+=` : Some o valor da esquerda ao da direita, e depois salva o valor (`foo += bar`);
	- `-=` : Subtraia o valor da esquerda ao da direita, e depois salva o valor (`foo -= bar`);
	- `*=` : Multiplique o valor da esquerda ao da direita, e depois salva o valor (`foo * = bar`);
	- `/=` : Divida o valor da esquerda ao da direita, e depois salva o valor (`foo /= foo`);
	- `%=` : Faça o módulo da esquerda ao da direita, e depois salva o valor (`foo %= foo`);
- Operadores Comparadores:
	-  ` == ` : Igualdade entre os 2 (`foo == foo`);
	- `!=` : Diferenças entre os 2 (`foo != foo`);
	- `>` : Esquerda é maior que a direita (`foo \> foo`);
	- `<` : Esquerda é menor que a direita (`foo < foo`);
	- `>=` : Esquerda é maior ou igual que a direita (`foo \>= foo`);
	- `<=` : Esquerda é menor ou igual que a direita (`foo <= foo`);
- Operadores Lógicos:
	- `&&` -> E lógico (`foo && foo`);
	- `||` -> OU lógico (`foo || foo`);
	- `!` -> NÃO lógico (`!foo`);
- Ao criar variáveis, ela pode receber uma "função" para resolver, e receber o resultado dela. Ex: `let x = 10; let y = x * 7`.

## Descoberta de testes
- Divisão inteira não aproxima, retorna o valor cheio.
## Links relacionados
- 

---
