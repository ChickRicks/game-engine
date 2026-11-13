---
status: Em andamento
criado: 2026/11/01
modificado: 2026-11-04
autor: ChickRicks
---
# Condicionais

## Resumo
Estrutura do ifs, if/else, else if e match
if (completo): `if foo {bar} else if foo2 {bar2} else {bar3}`.
match: `match foo { foo1 => bar1, ... _ => bar2}`.
## Conteúdo
- ifs possuem estrutura: `if foo {foo} else if foo2 {foo2} ... else {foo3}` (veja código 1). 
- Ifs também podem ser usados como "função" de uma variável, porém, em caso de if else, eles devem retornar o mesmo tipo de valor (veja código 2).
- Match possui estrutura `match foo { foo => bar, ...  _ => bar}`, sendo _ valor caso não esteja dentro dos outros (veja código 3).
- Match aceita uso de | caso alguns valores devam retornar o mesmo resultado (veja código 4).
- Similar ao if, também pode ser uma expressão, com as mesmas regras do if (os valores que retornam tem que ser do mesmo tipo) (veja código 5).
-  Para borrowing e Ownership: o bloco interno do `if` pode trocar o ownership de variáveis de escopos externos (mais detalhes em ownership e borrowing).
## Descoberta de testes
- `If` aceita apenas valores booleanos, números não tem tradução de true ou false (veja código 6).
- `match` não pede variáveis, mas sim algum literal (variável, valor ou expressão) (veja código 7).
## Códigos relacionados
Código 1:
```rust hl_lines="2-4" linenums="1"
fn main(){
	if false{} // É analisado primeiro.
	else if false{} // Depois esse, caso o if seja falso.
	else{} // Por fim esse, caso todos sejam falsos.
}
```
Código 2:
```rust hl_lines="3-4" linenums="1"
fn main(){
	let x = 10;
	let y = if x > 10 {20} else {30};
	// let z = if x > 10 {20} else {'b'} - Tipos diferentes de resultado, não compila.
}
```
Código 3:
```rust hl_lines="3-6" linenums="1"
fn main(){
	let x = 10;
	match x {
	1 => println!("1"),
	2 => println!("2"),
	_ => println!("3"),
	} // Printa 3, x não é 1 ou 2.
}
```
Código 4:
```rust hl_lines="3 5" linenums="1"
fn main(){
	let x = 5;
	match x {
	1 | 2 | 3 => println!("1"),
	4 | 5 | 6 => println!("2"),
	_ => println!("3"),
	} // Printa 2, x é 4 ou 5 ou 6.
}
```
Código 5:
```rust hl_lines="3 8" linenums="1"
fn main(){
	let x = 5;
	let y = match x {
		1 | 2 | 3 => 2,
		4 | 5 | 6 => 6,
		_ => 0,
	}; // y recebe 6
	/*let z = match x {
		1 | 2 | 3 => 2,
		4 | 5 | 6 => '1',
		_ => false,
	} // z não funcionaria, retorna valores variados.*/
}
```
Código 6:
```rust hl_lines="2-3" linenums="1"
fn main(){
	if true {println!("Aqui funciona");}
	// if 9 {println!("Aqui não funciona");}
}
```
Código 7:
```rust hl_lines="2" linenums="1"
fn main(){
	match 3 { // Válido
	1 => println!("1"),
	2 => println!("2"),
	_ => println!("3"),
	}
}
```
## Links externos relacionados
-  [w3school if.else](https://www.w3schools.com/rust/rust_if_else.php) e [w3school match](https://www.w3schools.com/rust/rust_match.php).
## Links
- 👈 **Anterior:** [Operadores](3-Operadores.md)
- ➡️ **Próximo:** [Laço de Repetição](5-Lacos-de-repeticao.md)

