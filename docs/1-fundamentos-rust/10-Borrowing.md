---
status: Em andamento
criado: 2026-11-02
modificado: 2026-11-02
autor: ChickRicks
---
# Borrowing

## Para conveniência:
Ao usar domínio, traduza para ownership. Ao usar emprestar, traduza para borrowing.

## Resumo
Pode-se passar a referência de valor de um dono para outra variável sem passar transferência usando `&`, que também precisa de um `mut` próprio para ser mutável, na estrutura `let mut foo = &mut bar`, sendo `bar` mutável.

## Conteúdo
- Referenciar é olhar o valor sem transferir o domínio.
- Reduz a quantidade de `clones()`, tornando o código mais rápido.
- Caso queira passar o conteúdo para outra variável sem passar o domínio, pode-se usar o símbolo `&` para isso (veja código 1).
- Para referências serem mutáveis, elas também tem que ter o `mut` próprio, na estrutura `let foo = &mut bar`, sendo `bar` mutável (veja código 2).
- O valor dono precisa ser mutável para que o valor copiado seja (veja código 2).
- Podem existir múltiplas referências imutáveis, porém 1 única referência mutável, e nenhum pode acontecer ao mesmo tempo (veja código 3).

## Descoberta de testes
- Referências podem vir de referências também (veja código 4).
- Uma variável que referencia outra, ao receber um novo valor, não referencia mais a antiga variável (veja código 5).

## Códigos relacionados
Código 1
```rust hl_lines="3" linenums="1"
fn main(){
	let x = "teste".to_string();
	let y = &x; // Empresta x.
}
```
Código 2:
```rust hl_lines="2-5" linenums="1"
fn main(){
	let mut x = "Str".to_string();
	let y = &mut x;
	y.push('1');
	println!("{}",y); // Acaba o referenciamento de x aqui. Printa Str1\n.
	println!("{}",x); // Printa Str1\n.
	let z = "Str2".to_string();
	//let w = &mut z; - Inválido, z não é mutável.
}
```
Código 3:
```rust hl_lines="6-7 13-14" linenums="1"
fn main(){
	let mut x = "Str".to_string();
	let y = &mut x;
	y.push('1'); // Muda também x incluindo 1.
	y.push_str("aaaa"); // Muda também x incluindo aaaa.
	//let z = &mut x; - Inválido, y ainda está emprestando mutável.
	//let w = &x; - Inválido, y possui está emprestando como mutável.
	println!("{}",y); // Printa Str1aaaa\n
	x = "Str".to_string();
	let v = &x;
	let u = &x;
	let t = &x;
	//let s = &mut x; - Inválido, existem referências não mutáveis de x ainda acontecendo.
	println!("{} {} {}",v,u,t); // Printa Str Str Str\n.
}
```
Código 4:
```rust hl_lines="3" linenums="1"
fn main(){
	let x = "Str".to_string();
	let y = &x;
	let z = &y;
}
```
Código 5
```rust hl_lines="5-6" linenums="1"
fn main(){
	let mut x = "Str";
	let mut y = &x;
	println!("{} {}",x,y); // Printa Str Str\n
	y = &"Str2";
	x = "Str1";
	println!("{} {}",x,y); // Possível printar, x não está sendo emprestado mais. Printa Str1 Str2\n
	/*y = &x;
	x = "Str2";
	println!("{} {}",x,y); - Impossível, x mudou de valor enquanto é emprestado.
*/
}
```

## Links externos relacionados
- [w3school Borrowing](https://www.w3schools.com/rust/rust_borrowing_references.php)

## Links
- 👈 **Anterior:** [Ownership](9-Ownership.md)
- ➡️ **Próximo:** [Array](Estruturas-de-dados/Array.md)
