
---
status: pendente
criado: 2026/10/31
atualizado: 2026/11/01
autor: ChickRicks
---
# Basics

## Resumo


## Conteúdo

- Println!("Conteúdo"); -> print com quebra de linha.
- Print!("Conteúdo"); -> print sem quebra de linha.
- Parênteses obrigatórios (println(Conteúdo); funciona, printlnConteúdo; não).
- Mais de um print possível, incluindo intercalado.
- Print!\n("Conteúdo"); funciona normalmente (espaços branco ignorados).
- Não serão ignorados espaços brancos dentro da palavra chave, mas dentro de conteúdo de string funciona (Cont\neúdo funciona).
- Ter uma "!" dentro de print! e println! demonstram ser macros.
- String do rust entende caractéres funcionais (\n para quebra de linha, \0 para vazio, etc).
- Comentários de linha única tem "//".
- Comentários de muitas linhas tem '/ * ' de começo e ' * /' no final.
-  Declaração de variável:" "let foo = foo"
-  Para chamar a variável em uma string (para um print, por exemplo), usa-se "{}"
- Naturalmente, "let foo = foo" criam variáveis que não mudam.
-  Quebras de linha nos espaços continuam ignorados (dado que não corte palavras chaves ou valores)
- Para variáveis que podem mudar facilmente, monta-se "let mut foo = foo;"
- lex x = foo; -> let x = foo2 é válido;
- Rust aceita inteiros, pontos flutuantes, caracteres, booleana, strings, entre outras estruturas.
- Tem como deixar explícito o chamado de tipo de variável usando: let foo: foo = foo
- Tipos de variável:
	- i32: Números inteiros (-inf,+inf);
	- u32: Números naturais + 0 (0,+inf);
	- f64: números de ponto flutuante;
	- char: um carácter único;
	- &str: uma string;
	- bool: booleana (V ou F);
- Print aceita os dados mostrados
- Constantes possuem estrutura const foo: foo = foo;
- A estrutura é obrigatória incluir o tipo da constante.
- Ideal usar letras maiúsculas para constantes, facilitam a diferenciação.
- Operadores aritméticos:
	- + -> Soma (foo + foo);
	- - -> Subtração (foo - foo);
	- * -> Multiplicação (foo * foo);
	- / -> Divisão (foo / foo);
	- % -> Resto da divisão/módulo (foo%foo);
- Operadores definidores de variável:
	- = -> Coloque o valor da direita a esquerda (foo = foo);
	- += -> Some o valor da esquerda ao da direita, e depois salva o valor (foo += foo);
	- -= -> Subtraia o valor da esquerda ao da direita, e depois salva o valor (foo -= foo);
	- * = -> Multiplique o valor da esquerda ao da direita, e depois salva o valor (foo * = foo);
	- /= -> Divida o valor da esquerda ao da direita, e depois salva o valor (foo /= foo);
	- %= -> Faça o módulo da esquerda ao da direita, e depois salva o valor (foo %= foo);
- Operadores Comparadores:
	-  == -> Igualdade entre os 2 (foo == foo);
	- != -> Diferenças entre os 2 (foo != foo);
	- > -> Esquerda é maior que a direita (foo > foo);
	- < -> Esquerda é menor que a direita (foo < foo);
	- >= Esquerda é maior ou igual que a direita (foo >= foo);
	- <= Esquerda é menor ou igual que a direita (foo <= foo);
- Operadores Lógicos:
	- && -> E lógico (foo && foo);
	- || -> OU lógico (foo || foo);
	- ! -> NÃO lógico (!foo);
- Ao criar variáveis, ela pode receber uma "função" para resolver, e receber o resultado dela. Ex: let x = 10; let y = x * 7
- ifs possuem estrutura: if foo {foo} (else if {foo})* else {foo}
- Ifs também podem ser usados como "função" de uma variável, porém, em caso de if else, eles devem retornar o mesmo valor
- Match possui estrutura match foo { foo => foo, _ => foo}, sendo _ valor caso não esteja dentro dos outros.
- Match aceita uso de | caso alguns valores devam retornar o mesmo resultado.
- Similar ao if, também pode ser uma "função", com as mesmas regras do if (os valores que retornam tem que ser do mesmo tipo).

## Links relacionados
- 

## Status
> [!NOTE] Progresso
> - [x] Estrutura criada
> - [ ] Conteúdo preenchido
> - [ ] Revisado

---
