---
status: Em andamento
criado: 2026-11-02
modificado: 2026-11-06
autor: ChickRicks
---
# Strings

## Resumo
String de literais: `foo.to_string()` ou `String::from("foo")` para copiar uma string; `push` e `push_str` para adicionar pedaços de texto definidos, `format!` para concatenar strings, `.len()` para o tamanho de string em bytes, e `chars().count()` em caracteres

## Conteúdo
- [Formatos de String](2-Variaveis-e-constantes.md#conteudo)(veja código 2 no link):
	- &str ,"imutável", em geral, literal, é uma referência;
	- String é mutável, tem ownership e tem uma heap, sempre dona;
- Duas formas de criar string de um literal (veja código 1): 
	- Usando `to_string()` logo após da variável (`let foo = bar.to_string()` para `&str`, e `let foo = "bar".to_string()` para literais);
	- Usando `String::from()` com o texto resultante dentro do `from`  `let foo = String::from("bar")`;
- `push_str` para adicionar textos a uma variável string (`foo.push_str("bar")`) (veja código 2).
- `push` para um caracter único (`foo.push('b')`) (veja código 2).
-  Para `push` e `push_str` funcionarem, a variável que está sendo afetada precisa ser mutável (veja código 2).
- Duas formas de concatenar strings (veja código 3):
	-  Macro `format!` com os textos a serem concatenados (`foo = format!("foo {} {}",bar1,bar2)`), sem consumir as variáveis, apenas as copiando;
	-  Usando o operador `+` , porém menos recomendado (`foo = bar1 + bar2 + bar3` + ...), já que usar `+` acaba consumindo a string a esquerda. `bar2`, `bar3` e os que vem depois tem que ser strings fixas `&str`;
- `.len()` em uma string para retornar seu valor em bytes (`foo.len()`) e `.chars().count()` para contagem de caracteres (`foo.chars().count()`) (veja código 4).
- Ao usar strings em uma função, ela perde o domínio, a não ser que use `.clone()` para passar uma cópia dela (veja código 5).

## Descoberta de testes
- `format!` também concatena valores não string (veja código  6).

## Códigos relacionados
Código 1:
```rust hl_lines="2 4-5" linenums="1"
fn main(){
	let x: String = "Caso 1".to_string();
	let y_s: &str = "Caso 2";
	let y_S: String = y_s.to_string();
	let z: String = String::from("Caso 3");
}
```
Código 2:
```rust hl_lines="4-7" linenums="1"
fn main(){
	let mut x = "".to_string();
	let y = "".to_string();
	x.push('G');
	x.push_str("rande aumento.");
	// y.push('E'); - Inválido: y não é mutável
	// y.push_str("rro grotesco"); - Inválido: y não é mutável
}
```
Código 3:
```rust hl_lines="4-5" linenums="1"
fn main(){
	let x = "teste 1".to_string();
	let y = "teste 2".to_string();
	let result_1 = format!("{} {}",x,y);
	let result_2 = x + " " + &y; // Para funcionar, y tem que ser referenciado, usando &str ao invés de String.
}
```
Código 4:
```rust hl_lines="3 4" linenums="1"
fn main(){
	let x = "Teste de tamanho".to_string();
	let y = "Testes com mudanças".to_string();
	println!("{} {}",x.len(),x.chars().count()); // Retorna 16 16\n
	println!("{} {}",y.len(),y.chars().count()); // Retorna 20 19\n
	// len() usa a quantidade de bytes, enquanto chars().count() conta a quantidade de caracteres, importante caso usa a tabela ASCII expandida
}
```
Código 5
```rust hl_lines="3 5" linenums="1"
fn main(){
	let x = "Teste".to_string();
	teste(x.clone()); // .clone() vai ter mais detalhes quando chegar ownership.
	println!("{}",x);
	teste(x); // Depois daqui x não pode ser chamado sem re-declarar.
}
fn teste(mut var1: String){
	var1.push('1');
	println!("{}",var1);
}
```
Código 6
```rust hl_lines="5" linenums="1"
fn main(){
	let x = "teste";
	let y = 10;
	let z = 'a';
	let result = format!("{} {} {}",x,y,z);

}
```
## Links externos relacionados
- [w3school strings](https://www.w3schools.com/rust/rust_strings.php)

## Links
- 👈 **Anterior:** [Escopo](7-Escopo.md)
- ➡️ **Próximo:** [Ownership](9-Ownership.md)
