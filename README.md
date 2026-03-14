# 🤖 DocAI- Módulo de Extração e Armazenamento - Em Desenvolvimento 

Este módulo é responsável por processar documentos (PDFs), extrair seus textos e tabelas, aplicar limpeza de dados e armazenar as informações estruturadas em um banco de dados relacional para alimentar o sistema RAG.

## 🛠️ Funcionalidades Atuais

- **Extração de Texto e Tabelas:** Recuperação integral do conteúdo por página utilizando `pdfplumber`.
- **Sanitização de Dados (Data Cleaning):** - Remoção automática de valores nulos (`None`).
  - Limpeza de quebras de linha e espaços excedentes nas células das tabelas.
- **Integração com PostgreSQL:** - Criação automatizada de tabelas via script.
  - Armazenamento de textos longos (`TEXT`) e tabelas estruturadas nativamente como `JSONB`.
- **Segurança:** Uso de variáveis de ambiente (`.env`) para proteção das credenciais do banco de dados.

## 🚀 Tecnologias Utilizadas
* **Python**
* **pdfplumber:** Extração de coordenadas de texto e tabelas de PDFs.
* **PostgreSQL & psycopg2:** Banco de dados e driver de conexão.
* **python-dotenv:** Gerenciamento de variáveis de ambiente.

## 📂 Estrutura de Pastas
```text
backend/
└── code/
    ├── extract.py      # Script principal de extração e envio para o banco
    ├── database.py     # Setup das tabelas e funções de inserção (SQL)
    ├── .env            # Credenciais do banco (Não versionado)
    ├── input/          # Diretório de PDFs para processamento
    └── output/         # JSONs de backup gerados após a extração
