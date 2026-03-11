import pdfplumber
import os
import json
from database import insert_date


DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(DIRETORIO_ATUAL, "input", "PPCBCC2019.pdf")
filename = os.path.basename(path)

print("Versão do pdfplumber:", pdfplumber.__version__) #validacao 


def clearTable(rawTables):
    tabelas_limpas = []
    
    for tabela in rawTables:
        tabela_processada = []
        
        for linha in tabela:
            # 3. Limpa cada célula: tira None, tira \n e espaços extras
            linha_limpa = [
                str(celula).replace('\n', ' ').strip() if celula is not None else "" 
                for celula in linha
            ]
            tabela_processada.append(linha_limpa)
        tabelas_limpas.append(tabela_processada)
        
    return tabelas_limpas


def extract_Dados(path):
    splinedData = {}#guardar os textos extraidos
    with pdfplumber.open(path) as pdf:
        #print(len(pdf.pages))
        for i, pagina in enumerate(pdf.pages):
            textPage = pagina.extract_text()
            textTable= pagina.extract_tables()
            cleanTables = clearTable(textTable)
            splinedData[f"pagina-{i+1}"] = {
                "texto": textPage,
                "tables": cleanTables
                }

            insert_date(filename, i+1, textPage, cleanTables) #chamada funcão do database.py

            print(f"Página {i+1} processada e enviada ao banco!")
        outputDir = os.path.join(DIRETORIO_ATUAL, "output")
        os.makedirs(outputDir, exist_ok=True)
        pathJson = os.path.join(outputDir, "dados.json")
        os.makedirs(pathJson, exist_ok=True)
        pathJson = os.path.join(pathJson, "dados.json")
        with open(pathJson, 'w', encoding='utf-8') as f:
            json.dump(splinedData, f, indent=4, ensure_ascii=False)
    return splinedData

if __name__ == "__main__":
    print("Extraindo Dados")
    result = extract_Dados(path)
    print("Enviado com sucesso verificar pgadmin")