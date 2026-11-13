---
status: Em andamento
criado: 2026-11-01
modificado: 2026-11-06
autor: ChickRicks
---
# Escopo

## Resumo
Variáveis ficam no escopo definido, que é definido pela quantidade de {} que está aninhado (incluindo funções).

## Conteúdo
- Blocos são separados por {} (veja código 1).
- Variáveis existem apenas no seu bloco. Funções, `if`,`for`,`while` e `match` criam blocos. `match` cria um bloco por braço(veja código 1). 
- [Pode-se repetir as mesmas variáveis no mesmo escopo](2-Variaveis-e-constantes.md#descoberta-de-testes) (veja código 5 do link).
- Ao sair do bloco em que está, o valor e descartado e o identificador deixa de ser válido (dado reatribuições futuras) (veja código 2).
- Pode também repetir a declaração de variáveis em escopos diferentes, e ela é tratada como uma nova (veja código 2).

## Descoberta de testes
- Novos escopos podem ser abertos sem uma função (veja código 3).
- Mudanças no valor dentro de um escopo muda o valor da variável do escopo externo, respeitando se a variável é mutável e não for shadowing (veja código 4).
## Códigos relacionados
Código 1
```rust hl_lines="1 3 5 9 11 15-17" linenums="1"
// Escopo 1 (global).
fn main(){
	// Escopo 2 (local a main).
	if true{
		// Escopo 3.1 (local ao if acima).
		break;
	}
	loop{
		// Escopo 3.2 (local ao loop acima).
		if false{
			//Escopo 4 (local ao if acima).
		}
	}
	match 2 {
		1 => true || true, // Escopo 3.3 (local ao braço do match acima).
		2 => false || false, // Escopo 3.4 (local ao braço do match acima).
		_ => true || false // Escopo 3.5 (local ao braço do match acima).
	}
	// Esse código retorna um warning (valores no match não retornam a algum lugar)
}
```
Código 2
```rust hl_lines="4-6" linenums="1"
fn main(){
	let x = 0;
	if true{
		let y = 0; 
		let x = 10; // Válido.
	} // Depois daqui, y some da memória, como valor, e o x local também, voltando ao valor de x do escopo anterior.
}
```
Código 3
```rust hl_lines="2-7" linenums="1"
fn main(){
	{
		// Válido.
		{
			// Válido também.
		}
	}
}
```
Código 4
```rust hl_lines="2 4" linenums="1"
fn main(){
	let mut x = 10;
	let y = 10;
	if true{
		x = 20;
	}
	println!("{}",x); // Vai printar 20\n.
	if true{
		// y = 20; - Inválido, y não é mutável
		let x = 15;
		println!("{} {}",x,y); // vai printar 15 10\n.
	}
	println!("{}",x); // vai printar 20\n.
}
```
## Links externos relacionados
- [w3school scope](https://www.w3schools.com/rust/rust_scope.php)
## Links
- 👈 **Anterior:** [Funções](6-Funcoes.md)
- ➡️ **Próximo:** [Strings](8-Strings.md)
