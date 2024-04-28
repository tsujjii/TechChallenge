from fastapi import APIRouter
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse, Response
from ..usecases.data_production import RequestProduction, ProductionUsecase
from ..usecases.data_processing import RequestProcessing, ProcessingUsecase

app = FastAPI()

production_router = APIRouter()
processing_router = APIRouter()
comm_router = APIRouter()
import_router = APIRouter()
export_router = APIRouter()


@production_router.post('/get_production')
async def get_production(request: RequestProduction):
    """Produção de vinhos, sucos e derivados do Rio Grande do Sul"""
    try:
        usecase = ProductionUsecase(request)
        response = usecase.execute()
        #TODO Criar um objeto de resposta, optando pelo retorno do dataset ou apenas um 204
        return JSONResponse()
    except Exception as ex:
        return JSONResponse(content=f'Houve um problema ao realizar a solicitação: {ex}', status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@processing_router.post('/get_processing')
async def get_production(request: RequestProcessing):
    """Quantidade de uvas processadas no Rio Grande do Sul"""
    try:
        usecase = ProcessingUsecase(request)
        response = usecase.execute()
        #TODO Criar um objeto de resposta, optando pelo retorno do dataset ou apenas um 204
        return JSONResponse()
    except Exception as ex:
        return JSONResponse(content=f'Houve um problema ao realizar a solicitação: {ex}', status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)