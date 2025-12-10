ADA PDF Analyzer

Ferramenta CLI de análise estrutural e sumarização de PDFs utilizando IA Local.

Este projeto foi desenvolvido como parte do processo seletivo para a bolsa Trainee LLM do Projeto ADA (Assembly Digital Assistant). O objetivo é demonstrar domínio em Python, manipulação de arquivos e integração com Large Language Models (LLMs) rodando localmente.

Funcionalidades

* Obrigatórias (Implementadas)

* Análise Estatística: Contagem de páginas, tamanho do arquivo, total de palavras e tamanho do vocabulário.

* Top 10 Palavras: Identificação das palavras mais frequentes (filtrando stopwords).

* Extração de Imagens: Salva todas as imagens do PDF em uma pasta organizada (imagens/<nome_do_arquivo>/).

* Resumo com IA Local: Utiliza o modelo Qwen2.5-1.5B-Instruct (via Hugging Face) para gerar um resumo conciso do documento.

Diferenciais (Extras)

* Relatório Rico em Markdown: Ao usar a flag --save, o sistema gera um relatório visual (.md) contendo tabelas e o resumo, muito superior a um simples .txt.

*  Arquitetura Modular: Código separado em responsabilidades claras (cli, pdf, utils, llm).

* Tratamento de Exceções: Sistema robusto que valida arquivos e previne crashes durante a leitura ou extração.

* Truncagem Inteligente: Lógica para lidar com PDFs grandes, limitando a janela de contexto para evitar estouro de memória na IA.

* Código em Inglês / Interface em Português: Padrão de mercado no código, mas acessível para o usuário final.

Instalação

Pré-requisitos

* Python 3.9 ou superior.

* Recomenda-se o uso de um ambiente virtual (venv).

Passo a Passo

Clone o repositório:

git clone [https://github.com/SEU_USUARIO/NOME_DO_REPO.git](https://github.com/SEU_USUARIO/NOME_DO_REPO.git)
cd NOME_DO_REPO



Instale as dependências:

pip install -r requirements.txt



(Isso instalará PyMuPDF, Torch, Transformers e Accelerate).

Como Usar

O projeto funciona via linha de comando (CLI).

1. Análise Básica (Tela)

Exibe as estatísticas e o resumo da IA diretamente no terminal.

python ada.py documento.pdf



2. Análise Completa + Salvar Relatório

Gera o relatório Relatorio_documento.md e extrai as imagens para a pasta imagens/.

python ada.py documento.pdf --save



Nota: Na primeira execução, o sistema fará o download do modelo de IA (aprox. 3GB). Isso pode levar alguns minutos dependendo da sua conexão. Nas execuções seguintes, o carregamento é rápido.

Estrutura do Projeto

O projeto segue uma arquitetura modular para facilitar a manutenção e escalabilidade:

├── ada.py                 # Ponto de entrada (Main)
├── requirements.txt       # Dependências
├── .gitignore            # Arquivos ignorados pelo Git
├── src/
│   ├── cli/
│   │   └── arguments.py   # Gerenciamento do argparse
│   ├── llm/
│   │   ├── model.py       # Carregamento do modelo Qwen/Hugging Face
│   │   └── summarize.py   # Lógica de geração de texto
│   ├── pdf/
│   │   ├── extractor.py   # Leitura de metadados e texto (PyMuPDF)
│   │   └── images.py      # Extração de imagens binárias
│   └── utils/
│       ├── files.py       # Validação de caminhos e arquivos
│       ├── report.py      # Geração do relatório em Markdown
│       └── text.py        # Limpeza, stopwords e contagem de palavras



Pontos de Atenção para Avaliação

Gostaria de destacar os seguintes pontos na minha implementação:

Modularização: O código não é um script único gigante. Cada arquivo tem uma responsabilidade única (S.O.L.I.D principles), facilitando testes e leitura.

Integração com LLM: Uso do modelo Qwen 2.5 com detecção automática de hardware (CPU/GPU) e tratamento de Context Window para evitar erros em textos longos.

UX (Experiência do Usuário): Feedback constante no terminal sobre o que o programa está fazendo ("Extraindo...", "Gerando resumo...") e tratamento de erros amigável.

Qualidade da Saída: A escolha de gerar um relatório em Markdown ao invés de texto puro demonstra preocupação com a entrega final da informação.

Autor: Felipe Alves Lopes