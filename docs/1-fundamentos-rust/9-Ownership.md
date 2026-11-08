---
status: Em andamento
criado: 2026-11-02
modificado: 2026-11-06
autor: ChickRicks
---
# Ownership

## Resumo
Um valor possui apenas um dono, e pode emprestar a outras, sem deixar de ser dona.

## Conteúdo
- Montada planejada para manter o uso de memória segura, sem uso de garbage collector de memória.
- Um valor possui um único dono (veja código 1).
- Quando o dono sai de escopo, ele é removido da memória (veja código 1).
- [Existem formas de "emprestar" o valor](10-Borrowing.md#conteudo), mas em geral só existe um dono do valor.
- Variáveis complexas trocam de dono, variáveis simples copiam seu valor para frente (veja código 2).
	- Variáveis simples(copy): i32,bool,char,&str;
	- Variáveis complexas(move): String, Vec;
- `.clone()` pode ser usado para copiar valores para outra variável, sem trocar o dono do valor (veja código 3).

## Descoberta de testes
- `&str` é considerado uma variável simples, enquanto `String` é considerado uma variável complexa (veja código 4).

## Códigos relacionados
Código 1:
```rust hl_lines="3 5-6" linenums="1"
fn main(){
	let x = "teste".to_string();
	let y = x; // y recebe o domínio de x.
	if true{
		let z = 12;
	} // Daqui, z deixa de existir na memória.
}
```
Código 2:
```rust hl_lines="3 5" linenums="1"
fn main(){
	let x1 = 10;
	let y1 = x1; // Aqui simplesmente copia o valor.
	let x2 = "teste".to_string();
	let y2 = x2; // Aqui faz a troca de domínio de x2 para y2.
}
```
Código 3:
```rust hl_lines="2-3" linenums="1"
fn main(){
	let x = "String".to_string();
	let y = x.clone(); // Cria uma cópia de x e faz y ser dono dessa cópia.
	let z = x; // Simplesmente troca o domínio.
}
```
Código 4:
```rust hl_lines="3 5-7" linenums="1"
fn main(){
	let x1 = "&str";
	let y1 = x1;
	let x2 = "String".to_string();
	let y2 = x2;
	println!("{}",x1); // Print possível, x1 continua existindo
	// println!("{}",x2); - Print impossível, x2 deixou de ser dono do conteúdo.
}
```
## Links externos relacionados
- [w3school Ownership](https://www.w3schools.com/rust/rust_ownership.php)

## Links
- 👈 **Anterior:** [Strings](8-Strings.md)
- ➡️ **Próximo:** [Borrowing](10-Borrowing.md)
