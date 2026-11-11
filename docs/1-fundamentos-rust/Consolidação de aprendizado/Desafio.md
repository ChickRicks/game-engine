# Árvore binária de busca rubro negra esquerdista

Montar uma árvore binária de busca rubro negra esquerdista

Funcionamento:

Árvore: A árvore é composta por uma estrutura de "nós" ou folhas.
Binária: Cada nó possui, no máximo, dois filhos diretamente abaixo dele.
BST: Um tipo específico de árvore, no qual filhos a esquerda são "Menores" comparado ao valor pai, e filhos a direita são "Maiores" comparado ao valor pai.
Árvore binária de busca rubro negra esquerdista: Uma árvore binária de busca autobalanceável, com as seguintes propriedades:
1. Nós possuem uma cor: preta ou vermelha.
2. Nós vermelhos são necessariamente filhos de um nó preto, e sempre estão a esquerda
3. O plano é ser autobalanceável equilibrando nós vermelhos e pretos
4. A raiz é sempre preta (para questões de autobalanceamento).
Para a árvore ser plausível:
 5. Nós sempre serão colocados como vermelhos.
 6. Eles se arrumaram recursivamente, verificando se estão corretos ou não, de forma pós-verificada (analisa os filhos da árvore primeiro, depois analisa a si).
 7. Terá 3 funções principais:
	 1. Girar a esquerda: Caso o filho a direita seja vermelho e o filho a esquerda preto, a rotação a esquerda resolve o problema localmente.
	 2. Girar a direita: Caso o filho a esquerda seja vermelho, E o filho a esquerda dele também, é realizado uma rotação a direita.
	 3. Subida de cor: Caso os dois filhos sejam vermelhos durante as correções, os filhos viram nós pretos e o pai vira um nó vermelho.
	 4. As funções foram colocadas na ordem que acontece (primeiro rotações a esquerda, depois rotações a direita, e, por fim, a subida de cor).
8. Remover envolve alguns cenários extras