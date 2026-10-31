# Motor Gráfico em Rust

Documentação do desenvolvimento de um motor de jogos geral, escrito em Rust.

## Sobre este projeto

Registro da trilha de estudos, decisões técnicas e progresso na construção
de um motor próprio — cobrindo renderização com wgpu, arquitetura ECS,
entrada, áudio e física.

Cada seção abaixo corresponde a uma pasta em `docs/` e funciona como um
mini-projeto independente, com material teórico e registro do que foi
implementado.

## Navegação rápida

- **[Fundamentos de Rust](1.%20fundamentos-rust/index.md)** — ownership, borrowing,
  lifetimes e traits, a base necessária antes de encostar em gráficos.

- **[Matemática para Gráficos](2.%20matematica-graficos/index.md)** — revisão
  direcionada de álgebra linear: matrizes de transformação, coordenadas
  homogêneas e quaternions.

- **[Fundamentos de Computação Gráfica](3.%20fundamentos-graficos/index.md)** —
  pipeline gráfico, rasterização, shaders e depth buffer, independente de API.

- **[GPU com wgpu](4.%20gpu-wgpu/index.md)** — a API moderna de GPU em Rust,
  portável entre Vulkan, Metal, DirectX 12 e WebGPU.

- **[Arquitetura de Motor](5.%20arquitetura-motor/index.md)** — game loop, gestão
  de recursos, ECS e design orientado a dados.

- **[Subsistemas](6.%20subsistemas/index.md)** — entrada, áudio, física e
  serialização de cena.

## Status

Projeto em fase inicial de estudos.
