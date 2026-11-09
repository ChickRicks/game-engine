---
status: Em andamento
criado: 2026-11-08
modificado: 2026-11-08
autor: ChickRicks
---
# Hashmap

## Resumo
Precisa da biblioteca `use std::collections::HashMap;`. Para criar, usa `let mut foo = HashMap::new();`.Para inserir algo na hashmap, usa `insert()` com a estrutura `foo.insert(chave,valor)`. Para acessar, precisa usar `get()` na estrutura `foo.get(chave)`, retornando o valor. Pode atualizar os valores de uma chave usando o `insert()`. Pode ser valor de um `for`.

## Conteúdo
- HashMap é uma estrutura que guarda um grupo de 2 valores: um sendo a chave do valor, e o outro sendo o valor.
- Para criar um Hashmap, além de usar a biblioteca `use std::collections::HashMap;`, precisa usar a estrutura `let mut foo = HashMap::new()`. Mut é usado pois a HashMap vem vazia, e estaria permanentemente vazia sem ele (veja código 1).
- Para inserir valores na HashMap, usa a função `insert()` na estrutura `foo.insert(chave,valor)`(veja código 1).
- Para acessar os valores de uma HashMap, usa o comando `get(key)`, na estrutura `foo.get(key)` (veja código 2).
- Pode atualizar valores de uma hashmap usando o próprio `insert()`, apenas falar o nome da chave existente (veja código 3).
- Para remover valores de uma HashMap, usa a função `remove(key)`, na estrutura `foo.remove(key)` (veja código 4).
- Um HashMap pode ser referenciado em um for, para ele poder falar cada valor e chave, com a estrutura `for (key,value) in &hashmap{}`, sendo que `key` passaria por cada chave, e `value` passaria por cada valor relacionado (veja código 5).

## Descoberta de testes
- Chaves e valores podem ter tipos variados, incluindo outras estruturas de dados (veja código 6).
- A Hashmap pode conter apenas 1 tipo de valor (i32,u32,etc) tanto nas chaves quanto nos seu valores (veja código 7).
- Se não passar a referência da hashmap no `for`, ele move seus valores ao for, igual ao vector
- Ao usar `get()`, ele retorna `Some(value)` se existe, ou `None` se não existir. `Some()` é a referência do valor citado.
## Códigos relacionados
Exceto o código 1, assuma que x seja um hashmap com os valores:
(1,"Um")
(2,"Dois")
(3,"Três")
Códigos com outras variáveis terão sua estrutura montada.
Código 1:
```rust hl_lines="1 3-6" linenums="1"
use std::collections::HashMap;
fn main(){
	let mut x = HashMap::new();
	x.insert(1,"Banana"); // Agora a chave 1 contém "Banana".
	x.insert(2,"Maçã"); // Agora a chave 2 contém "Maçã".
	let y = HashMap::new(); // HashMap que sempre estará vazia, pois não tem como inserir novos valores, pela falta de mut.
}
```
Código 2:
```rust hl_lines="5" linenums="1"
use std::collections::HashMap;
fn main(){
	let mut x = HashMap::new();
	// ... insere valores.
	println!("{:?} {:?}",x.get(1),x.get(3)); // Printa Some("Um") Some("Três")\n.

}
```
Código 3:
```rust hl_lines="5" linenums="1"
use std::collections::HashMap;
fn main(){
	let mut x = HashMap::new();
	// ... insere valores.
	x.insert(1,"Quatro"); // Substitui o antigo valor da chave 1 para "Quatro".
}
```
Código 4:
```rust hl_lines="5" linenums="1"
use std::collections::HashMap;
fn main(){
	let mut x = HashMap::new();
	// ... insere valores.
	x.remove(2); // Remove a combinação 2-"Dois"
}
```
Código 5:
```rust hl_lines="5-6" linenums="1"
use std::collections::HashMap;
fn main(){
	let mut x = HashMap::new();
	// ... insere valores.
	for (chave,valor) in &x{
		println!("{} {}", chave, valor); // Printa chave valor\n para cada valor de x em ordem qualquer.
	}
}
```
Código 6:
```rust hl_lines="5-6 8-9" linenums="1"
use std::collections::HashMap;
fn main(){
	let mut x = HashMap::new();
	let mut y = HashMap::new();
	x.insert('1',"Um");
	x.insert('2',"Dois");
	// -----
	y.insert("Um",1);
	y.insert("Dois",2);
}
```
Código 7:
```rust hl_lines="6-7" linenums="1"
use std::collections::HashMap;
fn main(){
	let mut x = HashMap::new();
	x.insert('1',"Um");
	x.insert('2',"Dois");
	//x.insert(3,"Três"); - Inválido: tipo de chave incorreta (usando char, tentando inserir i32).
	//x.insert('4',4 as u32); - Inválido: tipo de valor incorreta (usando &str, tentando inserir u32).
}
```
## Links externos relacionados

## Links
- 👈 **Anterior:** [XXX](XXX)
- ➡️ **Próximo:** [XXX](XXX)
