---
status: Em andamento
criado: 2026-11-02
modificado: 2026-11-07
autor: ChickRicks
---
# Array

## Resumo
Guarda múltiplos valores de mesmo tipo, usando `let foo = [bar1,bar2,...];`. Possui tamanho fixo na criação. Chama os valores com `foo[n]`, sendo que n começa em 0. Pode ver o tamanho usando `.len()`. Também pode-se printar a array inteira, usando `print!("{:?}",array);`.

## Conteúdo
-  Arrays são uma estrutura de dados que guardam múltiplos valores de mesmo tipo, e seu tamanho é fixo.
- Para criar uma array, usa a estrutura `let foo = [bar1,bar2,...];` (veja código 1).
- Assim como outras variáveis, pode ser mutável, tornando os valores dentro da array mutáveis (veja código 1).
- Para chamar um valor de uma array, usa a estrutura `foo[n]`, sendo que n começa em 0 e vai até o limite da array (veja código 1).
- Pode-se ver o tamanho de uma array usando o comando `foo.len()`, retornando o total de valores (veja código 2).
- Um laço `for` aceita variáveis arrays, passando por cada valor do for (veja código 3).
- Existe uma forma de printar uma array inteira, usando `{:?}` (veja código 4)

## Descoberta de testes
- Usar um `for` para printar os valores simples da array não move os valores da array simples, mas move os valores complexos (veja código 5).
## Códigos relacionados
Código 1:
```rust hl_lines="2-5" linenums="1"
fn main(){
	let x = [1,2,3,4,5]; // Cria uma array com os valores mostrados.
	let mut y = [6,7,8,9,0]; // Cria uma array mutável com os valores mostrados.
	y[0] = 1; // Aqui troca o valor do primeiro dado da array y.
	// x[0] = 6; - Inválido: x não é mutável.
	println!("{} {}",x[0],y[0]); // Printa na tela 1 1\n.
}
```
Código 2:
```rust hl_lines="4" linenums="1"
fn main(){
	let x = [1,2,3,4,5];
	let y = [1,2,3,4,5,6,7,8];
	println!("{} {}",x.len(),y.len()); // Printa 5 8\n.
}
```
Código 3:
```rust hl_lines="3" linenums="1"
fn main(){
	let x = [1,2,3,4,5];
	for num in x{
		println!("{}",num); // Printa cada valor de x, seguido com um \n.
	}
}
```
Código 4:
```rust hl_lines="3" linenums="1"
fn main(){
	let x = [1,2,3,4,5,6];
	println!("{:?}",x); // Printa [1,2,3,4,5,6]\n.
}
```
Código 5:
```rust hl_lines="4 6-7 9 11" linenums="1"
fn main(){
	let x = [1,7,2,1,2,9];
	for num in x{
		println!("{}",num); // Printando cada número para tentar exaurir, que no fim apenas copia os valores.
	}
	println!("{:?}",x); // Continua printando [1,7,2,1,2,9]\n
	let y =["a".to_string(),"b".to_string(),"c".to_string(),"d".to_string(),"e".to_string()];
	for texto in y{
		println!("{}",texto);
	}
	// println!("{:?}",y) - Inválido: possui valores que foram movidos para o for.
}
```
## Links externos relacionados
- [W3School arrays](https://www.w3schools.com/rust/rust_arrays.php)
## Links
- 👈 **Anterior:** [Tipos de estruturas](../11-Tipos-de-estruturas-de-dados.md)
- ➡️ **Próximo:** [Vectors](Vector.md)