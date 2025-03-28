from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

# Configuração do CORS para permitir requisições do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


df = pd.read_csv("operadoras.csv", delimiter=";", on_bad_lines="skip").fillna("")

@app.get("/buscar")
def buscar_operadora(q: str = Query(..., description="Termo de busca")):
    resultados = df[df.apply(lambda row: row.astype(str).str.contains(q, case=False, na=False).any(), axis=1)]

    # Selecionando as colunas desejadas
    colunas_desejadas = [
        "CNPJ", "Razao_Social", "Nome_Fantasia", "Modalidade", "Representante",
        "Numero", "Complemento", "Bairro", "Cidade", "UF", "CEP", "Telefone", "Endereco_eletronico"
    ]
    resultados = resultados[colunas_desejadas]

    return resultados.to_dict(orient="records")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
