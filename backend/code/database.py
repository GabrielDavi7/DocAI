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
    commands=(
        """
        CREATE TABLE IF NOT EXISTS extract_dados( 
            id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,          --gerador de id automatico
            name_arquivo VARCHAR(255) NOT NULL,                           --nome arquivo
            page_number INTEGER NOT NULL,                                 --numero pagina
            db_text TEXT,                                                 --texto extraido dos arquivos
            db_json_tables JSONB,                                         --tabelas em json
            date_extract TIMESTAMP DEFAULT CURRENT_TIMESTAMP              --data automatica
        )
        """,
    )
    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        for command in commands:
            cur.execute(command)

        conn.commit() #sobe as alteracoes 
        cur.close() #fecha o cusor
        print("Tabelas criadas no banco de dados")

    except Exception as e:
        print(f"Erro ao criar as tabelas no banco {e}")

    finally:
        if conn is not None:
            conn.close() #fecha a base de dados

def insert_page_data(arquivo_name, number_page, db_text, tabelas_json):
    #inserir dados da pagina no db

    query = """
    INSERT INTO extract_dados(name_arquivo, page_number, db_text, db_json_tables)
    VALUES (%s %s %s %s)
            """
    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(query(arquivo_name, number_page, db_text, json.dumbs(tabelas_json)))

        conn.commit()
        cur.close

    except Exception as e:
        print(f"Erro ao inserir dados da pagina {number_page}: no banco {e}")

    finally:
        if conn:
            conn.close()

if __name__ == "__main__": 
    create_table()