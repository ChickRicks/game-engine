---
status: Em andamento
criado: 2026-11-07
modificado: 2026-11-07
autor: ChickRicks
---
# Vector

## Resumo
Guarda múltiplos valores de mesmo tipo, e pode variar seu tamanho. Para montar, usa-se `let foo = vec![bar1,bar2,...];`. Possui funções iguais a da array, além de `push(valor)` para expandir o vector no final, e `pop()` para remover no final. Também pode usar `insert()` para inserir em um espaço específico, usando `foo.insert(índice,valor);` e `remove()`, na estrutura `foo.remove(índice);`.

## Conteúdo
- Vectors possuem uma estrutura similar às [arrays](Estruturas-de-dados/Array.md), porém podem mudar de tamanho.
- Para criar um vector, tem que usar a estrutura `let foo = vec![bar1,bar2,...];` (veja código 1).
- Para poder mudar o tamanho de um vector, primeiramente ele precisa ser mutável (veja código 1).
- Assim como arrays, pode-se usar a função `len()`, chama os seu valores usando `foo[n]`, com n saindo de 0, e printando inteiramente usando `{:?}` (veja código 2).
- Para adicionar valores no fim de um vector, usa a função `push(valor)`, e para remover o valor final, usa a função `pop()`, que retorna o valor removido (veja código 3).
- Para adicionar em um espaço específico, usa a função `insert(índice,valor)`, empurrando os valores para frente, e para remover um valor em um espaço específico, usa a função `remove(índice)`, puxando os valores após o índice para fechar o buraco e retornando o valor removido (veja código 4);
## Descoberta de testes
- Similarmente as arrays, vectors consomem os valores complexos, mas também consomem os simples (veja código 5).
## Códigos relacionados
Código 1:
```rust hl_lines="2-3" linenums="1"
fn main(){
	let x = vec![1,2,1,2,3,1,2,3,4]; // Esse vector não pode mudar de tamanho.
	let mut y = vec![4,5,6,4,5,6]; // Esse vector pode mudar de tamanho.
}
```
Código 2:
```rust hl_lines="3 5" linenums="1"
fn main(){
	let x = vec![1,2,1,2,3,1,2,3,4];
	for num in &x{ // A necessidade de &x é que vectors são consumidos em fors, melhor explicado no código 5.
		println!("{}",num); // Printa cada valor de x.
	}
	println!("{} {:?}",x.len(),x); // Printa 9 [1,2,1,2,3,1,2,3,4]\n
}
```
Código 3:
```rust hl_lines="3-5" linenums="1"
fn main(){
	let mut x = vec![1,2,3];
	x.push(2); // Adiciona 2 no fim de x. vector resultante: [1,2,3,2].
	x.push(8); // Adiciona 8 no fim de x. vector resultante: [1,2,3,2,8].
	x.pop(); // Remove o fim de x, sendo o 8. vector resultante: [1,2,3,2].
	println!("{:?}",x); // Printa [1,2,3,2]\n.
}
```
Código 4:
```rust hl_lines="3-4" linenums="1"
fn main(){
	let mut x = vec![1,6,4,2,5];
	x.insert(3,0); // Adiciona 0 no índice 3 do vector x, depois empurra. vector resultante: [1,6,4,0,2,5].
	x.remove(1); // Remove o valor no índice 1 do vector x, depois puxa os valores. vector resultante: [1,4,0,2,5].
	println!("{:?}",x); // Printa [1,4,0,2,5].
}
```
Código 5:
```rust hl_lines="3 6 8 11" linenums="1"
fn main(){
	let x = vec![1,7,2,1,2,9];
	for num in x{
		println!("{}",num); // Printando cada número para tentar exaurir, que no fim consome o vector.
	}
	//println!("{:?}",x); - Inválido: diferentemente de arrays, aqui foi consumido pelo for.
	let y = vec!["a".to_string(),"b".to_string(),"c".to_string(),"d".to_string(),"e".to_string()];
	for texto in y{
		println!("{}",texto);
	}
	// println!("{:?}",y); - Inválido: possui valores que foram movidos para o for.
}
```
## Links externos relacionados
- [W3School Vectors](https://www.w3schools.com/rust/rust_vectors.php)

## Links
- 👈 **Anterior:** [Arrays](Estruturas-de-dados/Array.md)
- ➡️ **Próximo:** [Tuples](Tuple.md)
