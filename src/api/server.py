from fastapi import FastAPI
from .router import processing_router, production_router, commercialization_router, import_router, export_router

app = FastAPI()

app.include_router(production_router, tags=["v1"])
app.include_router(processing_router, tags=["v1"])
app.include_router(commercialization_router, tags=["v1"])
app.include_router(import_router, tags=["v1"])
app.include_router(export_router, tags=["v1"])

app.title = "Tech Challenge | Vitivinicultura Embrapa "
app.description = """As rotas a seguir são responsáveis por realizar um scraping nas abas de Produção, Processamento, Comercialização, Importação, Exportação,
do site da Vitivinicultura Embrapa. 
*   A API foi desenvolvida com o intuito de atender as questões lenvantadas no desafio Tech Challenge. 
*   Aqui é possível verificar toda a documentação dos parâmetros para cada rota, assim como sua descrição.
*   Para todas as rotas, é possível retornar os dados em um arquivo CSV, ou apenas salvar internamente na própria aplicação.
"""
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)