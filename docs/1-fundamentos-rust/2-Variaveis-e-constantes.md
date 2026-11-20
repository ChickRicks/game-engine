---
status: Em andamento
criado: 2026/11/01
modificado: 2026/11/18
autor: ChickRicks
---
# Variáveis e Constantes

## Resumo

Estrutura de Variáveis e constantes.
Variável imutável: `let foo = bar;`
Variável mutável: `let mut foo = bar;`
Constante: `const foo1: foo2 = bar;`, sendo foo2 o tipo da constante.
??? example "UML exemplo de variáveis:"
	```mermaid
	flowchart TD
		A["Código"] --> B[let]
		B --> C{"Escopo Global?"}
		C -- Não --> D{"Nome de variável válido?"}
		C -- Sim --> E["Erro: variáveis devem estar dentro de escopos não globais"]
		D -- Sim --> F{"Possui mut? (afeta reatribuição futura, não a declaração de variáveis)"}
		D -- Não --> G["Erro léxico"]
		F -- Sim, mutável --> H{"Possui alguma especificação de tipo?"}
		F -- Não, imutável --> H
		H -- Não --> I{"Possui alguma atribuição de valor no escopo criado?"}
		I -- Não --> J["Erro semântico: a variável não possui tipo"]
		H -- Sim --> K["Variável declarada, e seu valor é guardado, caso possua."]
		I -- Sim --> K
		K --> L["Código"]
	```
??? example "UML exemplo de constantes:"
	```mermaid
	flowchart TD
		A["Código"] --> B[const]
		B --> C{"Nome de constante válido?"}
		C -- Sim --> D{"Possui especificação de tipo?"}
		C -- Não --> E["Erro léxico"]
		D -- Sim --> F{"Recebe valor no escopo criado?"}
		D -- Não --> G["Erro semântico: constantes precisam de especificação de tipo (i32, por exemplo)"]
		F -- Sim --> H["Salva seu valor no escopo atual"]
		F -- Não --> I["Erro semântico: constantes precisam ter valor no escopo criado"]
		H --> J["Código"]
	```
## Conteúdo
-  Declaração de variável: `let foo = bar;` (Veja código 1)
-  Para chamar a variável em um print, usa-se `{}`. (Veja código 1)
- Naturalmente, `let foo = bar;` criam variáveis que não mudam. (Veja código 1)
- Para variáveis que podem mudar facilmente, monta-se `let mut foo = bar;` (Veja código 1)
- Rust aceita inteiros, pontos flutuantes, caracteres, booleana, strings, entre outras estruturas. (veja código 2)
- Tem como deixar explícito o chamado de tipo de variável usando: `let foo: foo = bar;`.
- Tipos de variável: (veja código 2):
	- i32 ou i64: Números inteiros (-inf,+inf);
	- u32 ou u64: Números naturais + 0 (0,+inf);
	- f32 ou f64: números de ponto flutuante;
	- char: um carácter único;
	- &str: uma string fixa;
	- String: uma string que pode mudar;
	- bool: booleanos (V ou F);
- Print aceita os dados mostrados (veja código 2).
- Constantes possuem estrutura `const foo: foo2 = bar;`, sendo que foo2 é o tipo de variável (veja código 3).
- A estrutura é obrigatória incluir o tipo da constante (veja código 3).
- Ideal usar letras maiúsculas para constantes, facilitam a diferenciação (veja código 3).
- Variáveis podem produzir valores diferentes usando `foo as type`, sem mudar o tipo original da variável (veja código 4).

## Descoberta de testes
-  Quebras de linha nos espaços continuam ignorados (dado que não corte palavras-chave ou valores) (veja código 5).
- `let x = foo; let x = foo2;` é válido (shadowing) (veja código 6).
- `let foo = bar` fora de funções não funciona (sem variáveis globais), mas constantes podem (veja código 7).
- Não pode declarar variável sem existir alguma forma que consiga ligar a variável a um tipo de valor, seja uma atribuição de valor ou uma anotação explícita (veja código 8).
## Links externos relacionados
- [w3schools rust variables](https://www.w3schools.com/rust/rust_variables.php) até [w3schools constants](https://www.w3schools.com/rust/rust_constants.php).

## Códigos relacionados
Código 1:
```rust hl_lines="2-5" linenums="1"
fn main(){
	let x = 10;
	let mut y = 20;
	println!("{} {}",x,y); // Isso printa 10 20\n
	y *= x; // Válido, y é mutável
	//x += y; - Inválido, x é imutável
}
```
Código 2:
```rust hl_lines="2-7 9" linenums="1"
fn main(){
	let a: i32 = -1; // Número inteiro
	let b: u32 = 2; // Número natural
	let c: f64 = 57.98; // Número com precisão double
	let d: char = 'g'; // Caracter único
	let e: &str = "String Fixa";
	let f: String = "String Mutável".to_string(); // Precisa de alguma forma para converter a string, veja em strings.
	//let g: String = "Não funciona"; - Uma string mutável recebe uma string fixa
	let h: bool = false; // Booleano
	println!("{} {} {} {} {} {} {}",a,b,c,d,e,f,h); // Printa -1 2 57.98 g String Fixa String Mutável false\n
}
```
Código 3:
```rust hl_lines="2-4" linenums="1"
fn main(){
	const X: i32 = 10;
	//const Y = 90; - Inválido, sem tipo definido
	const z: char = '9'; // Válido, porém não recomendado
}
```
Código 4:
```rust hl_lines="3" linenums="1"
fn main(){
	let x: i32 = 9; 
	let y: u32 = x as u32; // Válido, x entrega o seu valor como um u32, se mantendo i32.
}
```
Código 5:
```rust hl_lines="2-10" linenums="1"
fn main(){
	let
	a
	=
	10;
	let
	b:
	i32
	=
	90;
	// Funcional, porém pouco legível
}
```
Código 6:
```rust hl_lines="2-3" linenums="1"
fn main(){
	let x = 10;
	let x = '1';
	// Funciona, chama-se "Shadowing" (melhor explicado com ownership e borrowing)
}
```
Código 7:
```rust hl_lines="1-2" linenums="1"
// let x = 10; - Não permitido, escopo global
const Y: u32 = 10; // Permitido, constantes podem ser criadas em escopo público
fn main(){
	let z = 20;
}
```
Código 8:
```rust hl_lines="3-6" linenums="1"
fn main(){
	let a = 0;
	//let b; - Inválido, não possui um tipo de variável.
	let c;
	c = 1; // Válido, variável possui atribuição
	let d: u32; // Válido, possui tipo declarado
}
```
## Links
- 👈 **Anterior:** [Prints e Comentários](1-Prints-e-comentarios.md)
- ➡️ **Próximo:** [Operadores](3-Operadores.md)