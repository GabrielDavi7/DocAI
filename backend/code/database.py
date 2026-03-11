#arquivo para comunicar com o pgadmin
import os
from psycopg2 import sql
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()


def get_connection():
    #para puxar os dados do .env
    return psycopg2.connect(
        name_db = os.getenv("DB_NAME"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASS"),
        host_db = os.getenv("DB_HOST"),
        port_db = os.getenv("DB_PORT")
    )

def create_Table():
    #criar tabela caso não tenha 
    commands=(
        """
        CREATE TABLE IF NOT EXISTS extract_dados( 
            id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,          #gerador de id automatico
            name_arquivo VARCHAR(255) NOT NULL,                           #nome arquivo
            page_number INTEGER NOT NULL,                                 #numero pagina
            db_text TEXT,                                                 #texto extraido dos arquivos
            db_json_tables JSONB,                                         #tabelas em json
            date_extract TIMESTAMP DEFAULT CURRENT_TIMESTAMP              #data automatica
        )
        """
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
        print("Erro ao criar as tabelas no banco")

    finally:
        if conn is not None:
            conn.close() #fecha a base de dados

if __name__ == "__main__": 
    create_Table()