---
status: Em andamento
criado: 2026/10/31
modificado: 2026-11-04
autor: ChickRicks
---
# Prints e Comentários

## Resumo

`println!(foo)` para print com quebra de linha, `print!(foo)` para prints sem a quebra, `//` para comentários de uma linha, `/* comentário */` para comentários de mais de uma linha.
## Conteúdo

- `println!("Conteúdo");` : print com quebra de linha (veja código 1).
- `print!("Conteúdo");` : print sem quebra de linha (veja código 1).
- Mais de um print possível, incluindo intercalado.
- Não serão ignorados espaços brancos dentro da palavra chave, mas dentro de conteúdo de string funciona (`Cont\neúdo` funciona, e ele considera o texto com uma quebra de linha).
- Ter uma "!" dentro de print! e println! demonstram ser macros.
- String do rust entende carácteres funcionais (\n para quebra de linha, \0 para byte nulo, etc).
- Comentários de linha única tem "//" (Veja código 2).
- Comentários de muitas linhas tem '/ * ' de começo e ' \*/' no final (veja código 2).
## Descoberta de teste
- `print!\n("Conteúdo");` funciona normalmente (espaços branco ignorados) (veja código 3).
- Parênteses obrigatórios (`println!("Conteúdo");` funciona, `println!"Conteúdo";` não, nem `println!) (veja código 4).
## Códigos relacionados
Código 1:
```rust hl_lines="2-3" linenums="1"
fn main(){
	println!("Hello world!"); // Retorna no terminal Hello world!\n
	print!("Hello world 2: Electric boogaloo"); // Retorna no terminal Hello world 2: Electric boogaloo.
}
```
Código 2:
```rust linenums="1"
// Isso é um comentário de uma única linha
/* E isso é um comentário de múltiplas linhas
para fechar, é necessário colocar */
```
Código 3:
```rust hl_lines="2-5" linenums="1"
fn main(){
	print!
	("Funciona normalmente");
	println!
	("Também funciona :)");
}
```
Código 4:
```rust hl_lines="4-5" linenums="1"
fn main(){
	println!("Funcionamento normal");
	print!("Normal até demais");
	//println!"Parece que algo está errado"; - não funciona por não ter parênteses
	//print!"Não sei dizer o quê"; - também não funciona
	//println!(Acho que não deveria me preocupar); // não funciona por não ter aspas
	//print!(Afinal, tudo está certo, né?); // também não funciona
	// Esse código não vai compilar, vide linhas 4 a 7
}
```

## Links externos relacionados
- [w3schools síntaxe](https://www.w3schools.com/rust/rust_syntax.php) até [w3schools comments](https://www.w3schools.com/rust/rust_comments.php).

## Links
- 👈 **Anterior:** [index](0-index.md)
- ➡️ **Próximo:** [Variaveis e Constantes](2-Variaveis-e-constantes.md)
---
