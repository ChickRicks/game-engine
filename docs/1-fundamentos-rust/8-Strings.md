---
status: Em andamento
criado: 2026-11-02
modificado: 2026-11-02
autor: ChickRicks
---
# Strings

## Resumo
String de literais: `foo.to_string()` ou `String::from("foo")` para copiar uma string; `push` e `push_str` para adicionar pedaços de texto definidos, `format!` para concatenar strings, `.len()` para o tamanho de string em bytes, e `chars().count()` em carácteres

## Conteúdo
- [Formatos de String:](2-Variaveis-e-constantes.md#conteudo)
	- &str ,imutável, em geral, literal, é uma referência;
	- String é mutável, tem ownership e tem uma heap, sempre dona;
- Duas formas de criar string de um literal: 
	- Usando `to_string()` logo após da variável (`let foo = bar.to_string()` para &str, e `let foo = "bar".to_string()` para literais);
	- Usando `String::from()` com o texto resultante dentro do `from`  `let foo = String::from("bar")`;
- `push_str` para adicionar textos a uma variável string (`foo.push_str("bar")`).
- `push` para um carácter único (`foo.push('b')`).
-  Para `push` e `push_str` funcionarem, a variável que está sendo afetada precisa ser mutável.
- Duas formas de concatenar strings:
	-  Macro `format!` com os textos a serem concatenados (`foo = format!("foo {} {}",bar1,bar2`) ), sem consumir as variáveis, apenas as copiando;
	-  Usando o operador `+` , porém menos recomendado (`foo = bar1 + bar2 + bar3`), já que usar `+` acaba consumindo a string a esquerda;
- `.len()` em uma string para retornar seu valor em bytes (`foo.len()`) e `.chars().count()` para contagem de carácteres (`foo.chars().count()).
- Ao usar &s a uma função pedindo uma string, ele retorna sua referência, não seu owning

## Descoberta de testes
- `format!` também concatena valores não string;

## Links externos relacionados

## Links
- 👈 **Anterior:** [Escopo](7-Escopo.md)
- ➡️ **Próximo:** [Ownership](9-Ownership.md)
