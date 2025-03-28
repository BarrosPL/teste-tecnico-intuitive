import pandas as pd
import zipfile
import os
from pdfplumber import open as pdf_open

ABREVIACOES = {
    "OD": "Seg. Odontológica",
    "AMB": "Seg. Ambulatorial"
}

def extrair_tabela_pdf(pdf_path):
    dados = []
    with pdf_open(pdf_path) as pdf:
        for page in pdf.pages:
            tables = page.extract_table()
            if tables:
                dados.extend(tables)
    return pd.DataFrame(dados[1:], columns=dados[0]) 

def processar_dados(df):
    for col in df.columns:
        if col in ABREVIACOES:
            df[col] = df[col].replace(ABREVIACOES)
    return df

def salvar_comprimir_csv(df, nome):
    csv_filename = f"Teste_{nome}.csv"
    zip_filename = f"Teste_{nome}.zip"
    df.to_csv(csv_filename, index=False, encoding='utf-8')
    
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(csv_filename)
    os.remove(csv_filename)
    print(f"Arquivo {zip_filename} gerado com sucesso!")

pdf_path = "anexo1.pdf"
nome_usuario = "Pedro_Lucas"  

df = extrair_tabela_pdf(pdf_path)
df = processar_dados(df)
salvar_comprimir_csv(df, nome_usuario)
