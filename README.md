# DocAI

Gerenciamento e análise de documentos. Através da implementação de uma arquitetura RAG, o sistema permite que usuários façam upload de arquivos PDF e interajam com o conteúdo através de uma interface de chat, obtendo respostas contextualizadas.

## 🛠️ Funcionalidades Atuais

### 📄 Módulo de Extração (Backend)
O sistema conta com um extrator desenvolvido em **Python**, capaz de processar documentos PDF e estruturar os dados para o Chatbot.

- **Extração de Texto:** Recuperação integral do conteúdo textual por página.
- **Processamento de Tabelas:** Identificação e extração de tabelas.
- **Sanitização de Dados (Data Cleaning):** - Remoção automática de valores nulos (`None`).
  - Limpeza de quebras de linha e espaços excedentes.
  - Formatação de células para compatibilidade com sistemas de IA.
- **Saída Estruturada:** Geração de arquivos JSON organizados por página, facilitando a futura indexação em bancos de dados.

## 🚀 Tecnologias Utilizadas no Módulo
* **Python 3.10+**
* **pdfplumber:** Para extração de coordenadas de texto e tabelas.
* **JSON/OS:** Para manipulação de arquivos e diretórios de saída.

## 📂 Estrutura de Pastas (Atualizada)
```text
backend/
└── code/
    ├── extract.py      # Script principal de extração e limpeza
    ├── input/          # PDFs para processamento (ignorado no git)
    └── output/         # JSONs gerados após a extração
