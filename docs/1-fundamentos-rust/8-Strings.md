---
status: pendente
criado: "2026-11-02"
modificado: "2026-11-02"
autor: ChickRicks
---
# Strings

## Resumo
String de literais: `foo.to_string` ou `String::from(foo)`; `push` e `push_str` para adicionar pedaços de texto definidos, `format!` para concatenar strings, `.len()` para o tamanho de stringx

## Conteúdo
- [Formatos de String:](2-Variaveis-e-constantes.md#conteudo)
- Duas formas de criar string de um literal: 
	- Usando `to_string()` logo após da variável (`let foo = bar.to_string()`);
	- Usando `String::from()` com o texto resultante dentro do `from`  \(`let foo = String::from(bar)`\);
- `push_str` para adicionar textos a uma variável string (`foo.push_str(bar)`).
- `push` para um carácter único (`foo.push(bar)`).
- Duas formas de concatenar strings:
	-  Macro `format!` com os textos a serem concatenados (foo = format!("foo {} {}",bar1,bar2));
	-  Usando o operador `+` , porém menos recomendado (foo = bar1 + bar2 + bar3);
- `.len()` em uma string para retornar seu valor (foo.len()).

## Descoberta de testes
- `format!` também concatena valores não string;

## Links externos relacionados

## Links
- 👈 **Anterior:** [XXX](XXX)
- ➡️ **Próximo:** [XXX](XXX)
