---
status: Em andamento
criado: 2026-11-08
modificado: 2026-11-08
autor: ChickRicks
---
# Tuple

## Resumo
Guarda múltiplos valores de diferentes tipos. É de tamanho fixo, possui a estrutura `let foo = (bar1,bar2,...);`, sendo chamada com `foo.n`, sendo n começando em 0. Pode ser "desempacotada", chamando variáveis para seus resultados na estrutura `let (foo1,foo2,...) = tuple`.

## Conteúdo
- Tuples são boas para guardar múltiplos valores variados, porém são estáticas.
- Para criar uma tuple, a estrutura é `let foo = (bar1,bar2,...);`, sendo que qualquer `bar` pode ter qualquer valor (veja código 1).
- Para printar uma tuple, usa-se o mesmo `{:?}`, printando os valores da tuple dentro de () (veja código 1).
- Valores de tuples são acessadas usando a estrutura `foo.n`, sendo n um valor entre 0 e o tamanho da tuple (veja código 2).
- Ao criar uma tuple, você está a "empacotando" em uma variável.
- Para "desempacotar" uma tuple, você cria uma variável para cada valor a desempacotar usando, assumuindo uma tuple `(foo1,foo2,...) = tuple;` (veja código 3).
- Tuples podem ser resultado de funções (veja código 4).

## Descoberta de testes
- Para "desempacotar" uma tuple, você precisa de uma equivalência de tamanho (veja código 5).
- Similar a arrays, tuples copiam valores simples e movem as complexas, incluindo no "desempacotamento" (veja código 6).

## Códigos relacionados
Código 1:
```rust hl_lines="2-3" linenums="1"
fn main(){
	let x = (1,'2',"Três");
	println!("{:?}",x); // Printa (1,'2',"Três")\n.
}
```
Código 2:
```rust hl_lines="3" linenums="1"
fn main(){
	let x = (1,'2',"Três");
	println!("{} {}",x.0,x.2); // Printa 1 Três\n.
}
```
Código 3:
```rust hl_lines="3" linenums="1"
fn main(){
	let x = (1,'2',"Três");
	let (y,z,w) = x; // Aqui y recebe 1, z recebe '2' e w recebe "Três"
}
```
Código 4:
```rust hl_lines="2 4-5" linenums="1"
fn main(){
	let x = result();
	println!("{:?}",x); // Printa (34,"teste")\n.
}
fn result() -> (i32,&str){
	return (34,"teste");
}
```
Código 5:
```rust hl_lines="3-5" linenums="1"
fn main(){
	let x = (1,'2',"Três");
	let (y,z,w) = x; // Funciona, mesmo tamanho.
	// let (v,u,t,s) = x; - Inválido: maior que o tamanho de x.
	// let (r,q) = x; - Inválido: menor que o tamanho de x. 
}
```
Código 6:
```rust hl_lines="4-7" linenums="1"
fn main(){
	let x = (1,'2');
	let y = ("Três","Quatro".to_string());
	let (z,w) = x; // Valores simples: são copiados.
	let (u,v) = y; // Copia o &str, move a String.
	println!("{:?}",x); // Ainda possível, nenhum valor foi movido.
	//println!("{:?}",y); - Inválido: y possui um valor movido ("Quatro"). 
}
```
## Links externos relacionados
- [W3School Tuples](https://www.w3schools.com/rust/rust_tuples.php)
## Links
- 👈 **Anterior:** [Vectors](Vector.md)
- ➡️ **Próximo:** [XXX](XXX)
