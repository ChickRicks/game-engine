---
status: pendente
criado: 2026-11-12
modificado: 2026-11-18
autor: ChickRicks
---
# Struct

## Resumo
Para criar uma struct, usa a estrutura `struct foo {foo1: bar1,foo2: bar2,...}`, para criar uma instância com valores da struct usa `let foo = nomeStruct {foo1: bar1, foo2: bar2,...}`, ou com `mut` incluso para torná-lo mutável.

## Conteúdo
- `struct` é um formato de dado que gera templates com múltiplos tipos de dados nomeados, e, similar a `tuples`, podem guardar tipos variados de dados.
- Para criar uma `struct`, além da palavra chave, também usa a estrutura `struct foo{foo1: bar1,foo2: bar2,...}`, sendo `fooN` o nome da variável, e `barN` o [tipo da variável](../2-Variaveis-e-constantes.md) (veja código 1).
- Depois de criada, a struct pode ser chamada na estrutura `let foo = struct {foo1: bar1, foo2: bar2,...}`, sendo `fooN` o nome da variável, e `barN` o valor que vai receber, respeitando a regra da struct original (veja código 1).
- Assim como variáveis, para mudar valores da instância gerada por uma struct, ela tem que conter `mut`, estando assim `let mut foo = struct {foo1: bar1, foo2: bar2,...}` (veja código 2).
- Para extrair os valores da struct que uma variável possui, usa-se a estrutura `struct.fooN`, assim retornando o valor que está em `fooN`(veja código 2).

## Descoberta de testes
- Os valores de uma struct não podem ser individualmente mutáveis, apenas a variável que contém a struct (veja código 3).

## Códigos relacionados
Código 1:
```rust hl_lines="2-11" linenums="1"
fn main(){
	struct teste {
		x: i32,
		y: u32,
		z: String
	}
	let w = teste{
		x: -8,
		y: 32,
		z: "Um texto de teste".to_string()
	};
	// Retorna warning de variável não usada (warning: unused variable)
}
```
Código 2:
```rust hl_lines="7 12 17-18" linenums="1"
fn main(){
	struct teste2 {
		x: u32,
		y: u64,
		z: f64
	}
	let w = teste2{
		x: 5,
		y: 10,
		z: 6.9
	};
	let mut u = teste2{
		x: 10,
		y: 7,
		z: 10.23
	};
	//w.x = 10; - Inválido: w não é uma variável mutável.
	u.y = 80; // Válido, u é mutável.
}
```
Código 3:
```rust hl_lines="7-8 10-12 16-17 19" linenums="1"
fn main(){
	struct teste3 {
		x: i64,
		y: f64,
		z: String
	}
	/*let w = teste3{
		mut x: 65,
		y: 90.5,
		mut z: "Essa struct não vai funcionar".to_string()
	} Inválido: os parâmetros x e z estão com mut, não exclusivamente o nome.*/
	let mut u = teste3{
		x: 10,
		y: 10.8,
		z: "Essa struct vai funcionar".to_string()
	} // Válido: não fere a estrutura da struct.
	/* let mut v = teste3{
		x: 29,
		mut y: 65.1
		z: "Essa struct vai quebrar também".to_String()
	} Inválido: o parâmetro y possui mut, não exclusivamente o nome.*/
}
```
## Links externos relacionados

## Links
- 👈 **Anterior:** [Hashmaps](Hashmap.md)
- ➡️ **Próximo:** [Enums](Enum.md)
