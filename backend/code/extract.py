import pdfplumber
import os
import json

print("Versão do pdfplumber:", pdfplumber.__version__) #validacao 
path = r"backend\code\input\PPCBCC2019.pdf"


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


def extractDados(path):
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
        pathJson = r"backend\code\output"
        os.makedirs(pathJson, exist_ok=True)
        pathJson = os.path.join(pathJson, "dados.json")
        with open(pathJson, 'w', encoding='utf-8') as f:
            json.dump(splinedData, f, indent=4, ensure_ascii=False)
    return splinedData

result = extractDados(path)
print("Extracao concluída com sucesso! Verifique a pasta output.")