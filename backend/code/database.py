#arquivo para comunicar com o pgadmin
import os
import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import json

# Carrega as variáveis do arquivo .env
load_dotenv()


def get_connection():
    #para puxar os dados do .env
    return psycopg2.connect(
        dbname = os.getenv("DB_NAME"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASS"),
        host = os.getenv("DB_HOST"),
        port = os.getenv("DB_PORT")
    )

def create_table():
    #criar tabela caso não tenha 
    command=(
        """
        CREATE TABLE IF NOT EXISTS extract_dados( 
            id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,          --gerador de id automatico
            name_arquivo VARCHAR(255) NOT NULL,                           --nome arquivo
            page_number INTEGER NOT NULL,                                 --numero pagina
            db_text TEXT,                                                 --texto extraido dos arquivos
            db_json_tables JSONB,                                         --tabelas em json
            date_extract TIMESTAMP DEFAULT CURRENT_TIMESTAMP              --data automatica
        )
        """
    )
    conn = None
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(command)
                conn.commit()
        print("Tabelas criadas no banco de dados")

    except Exception as e:
        print(f"Erro ao criar as tabelas no banco {e}")

def insert_date(arquivo_name, number_page, text, tables):
    query = """
    INSERT INTO extract_dados(name_arquivo, page_number, db_text, db_json_tables)
    VALUES (%s, %s, %s, %s)
    """
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cleanTables = json.dumps(tables)
                cur.execute(query,(arquivo_name, number_page, text, cleanTables))
                conn.commit()

    except Exception as e:
        print(f"Erro ao inserir pagina {number_page}: no banco de dados {e}")

if __name__ == "__main__": 
    create_table()