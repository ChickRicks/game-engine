// Função que renderiza os diagramas
function renderMermaid() {
  // Garante que o Mermaid está disponível e inicializado
  if (typeof mermaid !== 'undefined') {
    mermaid.initialize({
      startOnLoad: false, // Desativa o carregamento automático
      theme: 'default'    // ou 'dark', para se adaptar ao seu tema
    });
    // Procura por todos os blocos mermaid na página e renderiza
    mermaid.run({
      querySelector: '.mermaid'
    });
  }
}

// 1. Executa após o carregamento inicial da página
document$.subscribe(function() {
  renderMermaid();
});

// 2. Executa sempre que um bloco <details> (que é o que o ??? gera) for aberto
document.addEventListener('toggle', function(event) {
  // Verifica se o evento é de abertura de um <details>
  if (event.target.tagName === 'DETAILS' && event.target.open) {
    // Pequeno atraso para garantir que o conteúdo já está visível no DOM
    setTimeout(renderMermaid, 100);
  }
}, true); // O 'true' permite capturar o evento durante a fase de captura