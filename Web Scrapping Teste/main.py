import requests
from bs4 import BeautifulSoup
import os
import shutil

url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

links_pdf = []
for link in soup.find_all("a"):
    href = link.get("href")
    if href and href.endswith(".pdf"):
        if "Anexo_I" in href or "Anexo_II" in href:
            links_pdf.append(href)

if not os.path.exists("anexos"):
    os.makedirs("anexos")

for link_pdf in links_pdf:
    nome_arquivo = link_pdf.split("/")[-1]
    caminho_arquivo = os.path.join("anexos", nome_arquivo)
    response_pdf = requests.get(link_pdf)
    with open(caminho_arquivo, "wb") as arquivo_pdf:
        arquivo_pdf.write(response_pdf.content)

print("Downloads dos PDFs concluídos!")

import zipfile

caminho_zip = "anexos_compactados.zip"
with zipfile.ZipFile(caminho_zip, "w") as arquivo_zip:
    for nome_arquivo in os.listdir("anexos"):
        caminho_arquivo = os.path.join("anexos", nome_arquivo)
        arquivo_zip.write(caminho_arquivo, nome_arquivo)

shutil.rmtree("anexos")        

print("Compactação dos anexos concluída!")

