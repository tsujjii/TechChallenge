from fastapi import FastAPI, status, APIRouter
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
async def get_production(request: RequestProduction, response: Response):
    """Produção de vinhos, sucos e derivados do Rio Grande do Sul"""

    try:
        usecase = ProductionUsecase(request)
        ress = usecase.execute()

        if ress.empty:
            return JSONResponse(content="Não há dados a serem processados", status_code=status.HTTP_200_OK)

        if request.save_dataset_localy:
            ress.to_csv(f'src/data/producao.csv')
            return Response(status_code=status.HTTP_204_NO_CONTENT)   

        headers = {}
        headers["Content-Disposition"] = f"attachment; filename=producao.csv"
        headers["Content-Type"] = "csv"
        content = ress.to_csv(index=False) 
        return Response(headers=headers, content=content, status_code=status.HTTP_200_OK)
    except Exception as ex:
        return JSONResponse(content=f'Houve um problema ao realizar a solicitação: {ex}', status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@processing_router.post('/get_processing')
async def get_processing(request: RequestProcessing):
    """Quantidade de uvas processadas no Rio Grande do Sul"""

    try:
        usecase = ProcessingUsecase(request)
        ress = usecase.execute()
        if ress.empty:
            return JSONResponse(content="Não há dados a serem processados", status_code=status.HTTP_200_OK)
        
        if request.save_dataset_localy:
            ress.to_csv(f'src/data/processamento_{request.categoria.__str__()}.csv')
            return Response(status_code=status.HTTP_204_NO_CONTENT)   
  
        headers = {}
        headers["Content-Disposition"] = f"attachment; filename=processamento_{request.categoria.__str__()}.csv"
        headers["Content-Type"] = "csv"
        content = ress.to_csv(index=False) 
        return Response(headers=headers, content=content, status_code=status.HTTP_200_OK)
    except Exception as ex:
        return JSONResponse(content=f'Houve um problema ao realizar a solicitação: {ex}', status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)