# Motor Gráfico em Rust

Documentação do desenvolvimento de um motor de jogos geral, escrito em Rust.

!!! warning "Aviso sobre uso de IA:"
	Esse projeto foi escrito por humanos. Mas o projeto inteiro não foi 100% humano.
	Aonde teve uso de IA:
		
		Estruturação do mkdocs: a estrutura vista contendo 1-,2-,etc, foi feito por IA inicialmente. Qualquer mudança terá revisão minha, e potencialmente feito por mim.
		
		Correções: os textos vem dos meus aprendizados, incluindo os testes aleatórios para ver comportamento. Porém, é passado na IA para poder fazer as correções necessárias para diminuir ambiguidade ou para tornar o texto menos informal.
		
		Ferramentas: Eu não conheço todas as ferramentas que o mkdocs ou o obsidian (o escritor que estou usando para escrever meus conhecimentos) possuem. Uso a IA para poder expandir formas de expressar o conteúdo que criei.
		
		Testes: Ao final de cada capítulo, eu faço um teste de conhecimento para reduzir as incertezas que posso ter deixado para trás. As ideias serão feitas por mim, e serão verificadas com a IA como correção.
		
		Fontes de estudo: Existem formas diferentes de se estudar um tópico (início de rust, por exemplo). A IA junta as plataformas de estudo que seriam melhores para o meu estudo, facilitando a pesquisa de novas informações, sem substituir o meu estudo, já que a IA não está gerando o resumo para mim, apenas coletando aonde pesquisar.
		
	IAs usadas:
		
		Lumo: O início do projeto usava o lumo para fazer a estruturação inicial, porém sua duração limitada no plano gratuito era um peso grande no progresso do projeto.
		
		Deepseek: A troca aconteceu quando os projetos do lumo não possuem chat persistente no plano gratuito, então troquei para o deepseek para os usos previstos.
		
	Qualquer código gerado no andar do projeto será feito a mão, e testado com auxílio da IA, como previsto no aviso. Os códigos de ensinamento seguem a mesma ideia: são escritas por mim e corrigidas na IA, caso possua algum erro de compilação/de nomenclatura técnica.
## Sobre este projeto

Registro da trilha de estudos, decisões técnicas e progresso na construção
de um motor próprio — cobrindo renderização com wgpu, arquitetura ECS,
entrada, áudio e física.

Cada seção abaixo corresponde a uma pasta em `docs/` e funciona como um
mini-projeto independente, com material teórico e registro do que foi
implementado.

## Navegação rápida

- **[Fundamentos de Rust](1-fundamentos-rust/0-index.md)** — básico geral, ownership, borrowing, lifetimes e traits, a base necessária antes de encostar em gráficos.

- **[Matemática para Gráficos](2-matematica-graficos/index.md)** — revisão
  direcionada de álgebra linear: matrizes de transformação, coordenadas
  homogêneas e quaternions.

- **[Fundamentos de Computação Gráfica](3-fundamentos-graficos/index.md)** —
  pipeline gráfico, rasterização, shaders e depth buffer, independente de API.

- **[GPU com wgpu](4-gpu-wgpu/index.md)** — a API moderna de GPU em Rust,
  portável entre Vulkan, Metal, DirectX 12 e WebGPU.

- **[Arquitetura de Motor](5-arquitetura-motor/index.md)** — game loop, gestão
  de recursos, ECS e design orientado a dados.

- **[Subsistemas](6-subsistemas/index.md)** — entrada, áudio, física e
  serialização de cena.

## Status

Projeto em fase inicial de estudos.
