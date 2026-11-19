---
status: Em andamento
criado: 2026-11-01
modificado: 2026-11-05
autor: ChickRicks
---
# Funções

## Resumo
Estrutura completa: `fn foo(foo1: bar1) -> bar2{bar3}`. `return` para as funções que retornam algo.

## Conteúdo
- Funções são recomendadas a usarem `snake_case`.
- Função possui estrutura completa `fn foo(foo1) -> bar1{bar}`, parâmetros e retornos são opcionais (`foo1` e `bar1`)(veja código 1).
- Chamar uma função é `foo()` (veja código 1).
- Para funções que recebem mais de um valor, fica `fn foo(foo1: bar1, foo2: bar2){}` (veja código 2).
- O conteúdo de variáveis da função envolve `foo: tipo de var` (veja código 2).
- Para funções que retornam valores, usa-se `-> tipo de var` na criação. Todas retornam algo, caso não possua, retorna () (veja código 3).
- Para o retorno de funções, pode se usar `return` ou, na última linha, fazer a operação sem `;`(veja código 3).
- Passa ownership para as variáveis complexas caso não seja usado `&` com a variável (veja em [ownership](9-Ownership.md)).
- Funções em rust aceitam recursão (função chamando ela mesma) (veja código 4).

## Descoberta de testes
- `return` implícito compila sem avisos, mas pode reduzir legibilidade.
- O retorno implícito é exclusivo do fim do bloco, o pedido de `return` exige statement `()`, o que o `if` é, não podendo retornar os seus braços. (veja código 5).
- Em rust, recursão sem caso de parada eventualmente gera stack overflow, e depois aborta, não fica preso permanentemente.

## Códigos relacionados
Código 1:
```rust hl_lines="2 4" linenums="1"
fn main(){
	func1(); // Chama func1, que printa Hello func1\n.
}
fn func1(){
	println!("Hello func1");
}
```
Código 2:
```rust hl_lines="2 4-5" linenums="1"
fn main(){
	func2(-11, 2, 5); // Chama func2, que printa -11 2 15\n.
}
fn func2(valor1: i32,valor2: u32,mut valor3: i32){
	valor3 += 10;
	println!("{} {} {}",valor1,valor2,valor3);
}
```
Código 3:
```rust hl_lines="2 4-5" linenums="1"
fn main(){
	println!("{}",func3(4)); // Printa o resultado de func3 recebendo 4, que é 12\n.
	println!("{}",func4(3)); // Printa o resultado de func4 recebendo 3, que é -6\n.
}
fn func3(valor1: i32) -> i32{
	return valor1 * 3;	
}
fn func4(valor1: i32) -> i32{
	valor1*-2
}
```
Código 4:
```rust hl_lines="5-8" linenums="1"
fn main(){
	println!("{}",fat(10)); // retorna 3628800
	// println!("{}",fat(1000)); - Inválido: u64 overflow (excede o limite de bits do u64).
}
fn fat(n: u64) -> u64 {
	if n <= 1 {return 1;}
	return n*fat(n-1);
}
```
Código 5:
```rust hl_lines="2-4" linenums="1"
fn func1() -> i32{
	if false {return 0;} //Válido
	//else if false {1} - Inválido: É um statement, ele não retorna (), mas i32.
	2 // Válido
}
```

## Links externos relacionados
- [w3school functions](https://www.w3schools.com/rust/rust_functions.php)
## Links
- 👈 **Anterior:** [Laços de Repetição](5-Lacos-de-repeticao.md)
- ➡️ **Próximo:** [Escopo](7-Escopo.md)
