from fastapi import APIRouter
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse, Response
from ..usecases.data_production import RequestProduction, ProductionUsecase

app = FastAPI()

production_router = APIRouter()
processing_router = APIRouter()
comm_router = APIRouter()
import_router = APIRouter()
export_router = APIRouter()


@production_router.post('/get_production')
async def get_production(request: RequestProduction):
    try:
        usecase = ProductionUsecase(request)
        response = usecase.execute()
        return JSONResponse()
    except Exception as ex:
        return JSONResponse(content=f'Houve um problema ao realizar a solicitação: {ex}', status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)