---
status: Em andamento
criado: 2026/11/01
modificado: 2026-11-04
autor: ChickRicks
---

# Operadores

## Resumo
 Operadores válidos: `+`, `-`, `/`, `*`, `%`, ` =`, `+=`, `-=`, `*=`, `/=`, `%=`, ` ==`, `!=`, `>`, `<`, `>=`, `<=`, `&&`, `||`, `!`.

## Conteúdo
- Operadores aritméticos (veja código 1):
	- `+` : Soma (`foo + foo2`);
	- `-` : Subtração (`foo - foo2`);
	- `*` : Multiplicação (`foo * foo2`);
	- `/` : Divisão (`foo / foo2`);
	- `%` : Resto da divisão/módulo (`foo%foo2`);
- Operadores de atribuição (veja código 2):
	- ` = ` : Move o valor da direita para a esquerda em casos de variáveis complexas, ou copia em caso de variáveis simples (`foo = bar`);
	- `+=` : Some o valor da esquerda ao da direita, e depois salva o valor (`foo += bar` = `foo = foo + bar`);
	- `-=` : Subtraia o valor da esquerda ao da direita, e depois salva o valor (`foo -= bar` = `foo = foo - bar`);
	- `*=` : Multiplique o valor da esquerda ao da direita, e depois salva o valor (`foo *= bar` = ` foo = foo * bar`);
	- `/=` : Divida o valor da esquerda ao da direita, e depois salva o valor (`foo /= bar` = `foo = foo/bar`);
	- `%=` : Faça o módulo da esquerda ao da direita, e depois salva o valor (`foo %= bar` = `foo = foo % bar`);
- Operadores Comparadores (veja código 3):
	-  ` == ` : Igualdade entre os 2 (`foo == foo`);
	- `!=` : Diferenças entre os 2 (`foo != foo`);
	- `>` : Esquerda é maior que a direita (`foo > foo`);
	- `<` : Esquerda é menor que a direita (`foo < foo`);
	- `>=` : Esquerda é maior ou igual que a direita (`foo >= foo`);
	- `<=` : Esquerda é menor ou igual que a direita (`foo <= foo`);
- Operadores Lógicos (veja código 4):
	- `&&` -> E lógico (`foo && foo`);
	- `||` -> OU lógico (`foo || foo`);
	- `!` -> NÃO lógico (`!foo`);
- Operadores bitwise (veja código 5):
	- `&` -> E bit a bit (`foo & foo`);
	- `|` -> OU bit a bit (`foo| foo`);
	- `^` -> OU exclusivo bit a bit (`foo ^ foo`);
	- `<<` -> Shift de valor a esquerda (`foo << bar`);
	- `>>` -> Shift de valor a direita (`foo >> bar`);
- Se a parte esquerda de `&&` for falsa, ela retorna falso, sem avaliação da direita (veja código 6).
- Se a parte esquerda de `||` for verdadeira, ela retorna verdadeiro, sem avaliação da direita (veja código 6).
- Ao criar variáveis, ela pode receber uma "função" para resolver, e receber o resultado dela (veja código 7).

## Descoberta de testes
- Divisão inteira não aproxima, retorna o valor inteiro sem arredondar (Veja código 8).

## Códigos relacionados
Código 1:
```rust hl_lines="4" linenums="1"
fn main(){
	let x = 10;
	let y = 20;
	println!("{} {} {} {} {}",x+y,y-x,x*y,y/x,x%y);	// Retorna 30 10 200 2 10\n
	}
```
Código 2:
```rust hl_lines="3-8" linenums="1"
fn main(){
	let mut x = 1;
	x = 2; // Coloca o valor de x para 2
	x += 1; // Soma o valor de x em 1, e depois coloca de volta no x
	x -= 2; // Subtrai o valor de x em 2, e depois coloca de volta no x
	x *= 12; // Multiplica o valor de x por 12, e depois coloca de volta no x
	x /= 3; // Divide o valor de x por 3, e depois coloca de volta no x
	x %= 3; // Faz o módulo de x na base 3, e depois coloca de volta no x
}
```
Código 3:
```rust hl_lines="4-11" linenums="1"
fn main(){
	let x = 3;
	let y = 4;
	x == y; // Retorna false, ambos são diferentes
	x != y; // Retorna true, ambos são diferentes
	x > y; // Retorna false, x não é maior que y
	y > x; // Retorna true, y é maior que x
	x < y; // Retorna true, x é menor que y
	y < x; // Retorna false, y não é menor que x
	x >= y; // Retorna false, x não é maior ou igual a y
	x <= y; // Retorna true, x é menor ou igual a y
	// Como o resultado das comparações não está sendo aplicada, ele retorna um warning ao compilar esse código
}
```
Código 4:
```rust hl_lines="4-11" linenums="1"
fn main(){
	let x = true;
	let y = false;
	x && y; // Retorna false, y é falso
	x && x; // Retorna true, ambos são verdadeiros
	y && y; // Retorna false, y é falso
	x || y; // Retorna true, x é verdadeiro
	x || x; // Retorna true, x é verdadeiro
	y || y; // Retorna false, y é falso
	!x; // Retorna false, x é verdadeiro
	!y; // Retorna true, y é falso
	// Como o resultado das operações não está sendo aplicada, ele retorna um warning ao compilar esse código
}
```
Código 5:
```rust hl_lines="4-8" linenums="1"
fn main(){
	let x = 9;
	let y = 5;
	x & y; // Retorna 1, só possuem o 1 em comum
	x | y; // Retorna 13, possuem 1,4 e 8 como 1
	x ^ y; // Retorna 12, possuem 4 e 8 como 1 exclusivos, e 1 como 1 em conjunto.
	(x << 1); // x anda para esquerda 1 vez e vira 18.
	(y >> 1); // y anda para direita 1 vez, e vira 2.
	// Como o resultado das operações não está sendo aplicada, ele retorna um warning ao compilar esse código
}
```
Código 6:
```rust hl_lines="4-7" linenums="1"
fn main(){
	let x = true;
	let y = false;
	x && y; // Pede investigação do lado direito, x é verdadeiro e retorna false
	y && x; // Não pede investigação, y já é falso e retorna false
	y || x; // Pede investigação do lado direito, y é falso e retorna true
	x || y; // Não pede investigação, x já é verdadeiro e retorna true
	// Como o resultado das operações não está sendo aplicada, ele retorna um warning ao compilar esse código
}
```
Código 7:
```rust hl_lines="3-4" linenums="1"
fn main(){
	let x = 10; // Recebe 10
	let y = x * 7; // Recebe 70, o resultado de x * 7
	let z = y / 2; // Recebe 35, o resultado de y / 2
}
```
Código 8:
```rust hl_lines="3" linenums="1"
fn main(){
	let x: u32 = 10; // Declaração explícita para exemplo
	println!("{}", x/3); // Printa 3, resultado de divisão inteira
}
```

## Links externos relacionados
- [w3schools operators](https://www.w3schools.com/rust/rust_operators.php) e [w3schools booleans](https://www.w3schools.com/rust/rust_booleans.php).

## Links
- 👈 **Anterior:** [Variáveis e Constantes](2-Variaveis-e-constantes.md)
- ➡️ **Próximo:** [Condicionais](4-Condicionais.md)