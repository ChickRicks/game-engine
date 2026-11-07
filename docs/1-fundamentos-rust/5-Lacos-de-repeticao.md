---
status: Em andamento
criado: 2026-11-01
modificado: 2026-11-05
autor: ChickRicks
---
# Laços de repetição

## Resumo
Possuem 3:
	`loop{}` : loop infinito, parado apenas com break ou parando o código
	`while(foo){}` : loop acontece enquanto a condição estiver correta
	`for foo in foo..foo{}` : loop dentro de um alcance definido
`break` : para a função loop em questão
`continue` : pula para a próxima iteração do loop

## Conteúdo
- Existem 3 estruturas de laço de repetição: loop, while e for.
- `loop{bar}` faz um loop infinito, sem nenhuma limitação de parar (veja código 1).
- Um `break` faz com que o laço seja interrompido (Veja código 1).
- Caso não coloque uma condição de parada dentro com um `break`, ele precisa ser parado com ctrl + c.
- `loop{bar}` pode ser usado como uma "função" de variável, usando o break como um return (veja código 2).
- `while(foo) {bar}` faz o loop até a condição ser falsa (veja código 3).
- Caso a condição seja inicialmente falsa, ele não começa (veja código 3).
- Além da condição ser falsa, também pode ser parada por um break (veja código 4).
- `continue` faz com que o resto do while seja ignorado, mas continua funcionando (veja código 4).
- `for foo in foo1..foo2{bar}` cria um laço com restrições (veja código 5).
- `foo2` é o limite, sem estar incluso (veja código 5).
- Para `foo2` ser incluso, deve ser `for foo in foo1..=foo2{bar}` (veja código 5).
- A variável incremental (`foo`) aumenta sozinha escolhendo o próximo valor válido naturalmente.
- `break` e `continue` funcionam normalmente para o `for` (veja código 6).
- `for` consome o iterador, arrays ficam vazias no fim (mais detalhes em [ownership](9-Ownership.md) e [borrowing](10-Borrowing.md)).
## Descoberta de testes
-  Possui prioridade  de execução de cima pra baixo. `breaks` barram o que ia acontecer depois, e `continue` reverifica a condição, sem olhar o resto do corpo (veja código 7).
- No `for`, `foo1` e `foo2` podem ser variáveis criadas anteriormente (veja código 8).
- `foo1` e `foo2` do `for` é válido usar caracteres, e ele segue a ordem da tabela ASCII (veja código 9).
- `for` pede previsibilidade, enquanto `while` se comporta melhor com condições finais incertas (como arrays de tamanho não conhecido).
- `for` cria a variável que usará de incremento.
## Códigos relacionados
Código 1:
```rust hl_lines="3-8" linenums="1"
fn main(){
	let mut x = 0;
	loop{
		x += 1;
		if x == 10{
			break;
		}
	}
	loop{
	println!("Isso printa infinitamente"); // Tem que parar o programa para parar essa função
	}
}
```
Código 2:
```rust hl_lines="3-7" linenums="1"
fn main(){
	let mut count = 0;
	let x = loop{
		if count == 5{
			break count;
		}
		count += 1;
	} // Isso eventualmente retorna 5 para x
}
```
Código 3:
```rust hl_lines="3-5 7-9" linenums="1"
fn main(){
	let mut x = 0;
	while x < 10{
	println!("{}",x); // Vai printar de 0 a 9,com \n entre cada um	
	x += 1;
	}
	while x < 10{
	println!("{}",x); // Não chega a acontecer, x não é menor que 10
	x += 1;
	}
}
```
Código 4:
```rust hl_lines="5 8" linenums="1"
fn main(){
	let mut x = 0;
	while x < 10 {
		if x == 6 {
		x += 1;
		continue;
		}
		if x == 8 {
		break;
		}
	x += 1;
	println!("{}", x); //printa de 1 a 7, sem contar o 6
	}
}
```
Código 5:
```rust hl_lines="4-6 8-10" linenums="1"
fn main(){
	let mut result = 0;
	for x in 0..10{
		result += 1;
		println!("{}",result); // vai printar de 1 a 10, com quebra de linha entre cada um.
	}
	result = 0;
	for x in 0..=10{
		result += 1;
		println!("{}",result); // vai printar de 1 a 11, com quebra de linha entre cada um.
	}
}
```
Código 6:
```rust hl_lines="5 7" linenums="1"
fn main(){
	let mut x = 0;
	for i in 0..10{
		if i == 4 {continue;} // vai pular o x + 1 quando i for 4.
		x += 1;
		if i == 7 {break;} // vai ignorar o resto dos valores quando i for 7.
	}
	println!("{}",x); // vai printar 6\n
}
```
Código 7:
```rust hl_lines="6 11 15 20 24" linenums="1"
fn main(){
	let mut x = 1;
	let mut i = 0;
	loop{
		break;
		println!("{}",x); // Não printa, break acontece antes.
	}
	while (true){
		if x == 1{
			x += 1;
			continue; // Nada abaixo que está dentro do while vai acontecer quando x for 1.
		}
		println!("{}",x); // Esse printa depois de x não for 1.
		break;
		println!("{}",x); // Esse nunca printa (depois do break).
	}
	for i in 0..10{
		if i == 0{
			x += 1;
			continue; // Nada abaixo que está dentro do for vai acontecer quando i for 0.
		}
		println!("{}",x); // Esse vai printar quando i não for 0.
		break;
		println!("{}",x); // Esse nunca vai printar (depois do break).
	}
	// Código vai gerar warnings porque não alcança o que foi falado.
}
```
Código 8:
```rust hl_lines="5 8" linenums="1"
fn main(){
	let i = 0;
	let f = 10;
	for x in i..f{
		println!("{}",x); // Vai printar de 0 a 9
	}
	for x in i..=f{
		println!("{}",x); // Vai printar de 0 a 10
	}
}
```
Código 9:
```rust hl_lines="3 6 9" linenums="1"
fn main(){
	for x in 'a'..'d'{
		println!("{}",x); // Vai printar as letras a b c com quebra de linha entre cada uma
	}
	for x in 'a'..='d'{
		println!("{}",x); // Vai printar as letras a b c d com quebra de linha entre cada uma
	}
	for x in '7'..='D'{
		println!("{}",x); // Vai printar os valores entre '7' e 'D' ('D' incluso) com quebra de linha entre cada uma
	}
}
```
## Links externos relacionados

- De [w3school loops](https://www.w3schools.com/rust/rust_loops.php) Até [w3school for loops](https://www.w3schools.com/rust/rust_loops_for.php)

## Links
- 👈 **Anterior:** [Condicionais](4-Condicionais.md)
- ➡️ **Próximo:** [Funções](6-Funcoes.md)