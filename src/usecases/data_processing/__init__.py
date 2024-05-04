import re
import pandas as pd
from .dtos import RequestProcessing
from ...models.enums import EnumTabs
from ...models.utils import processa_usecase

class ProcessingUsecase():
    """
    Classe responsável por executar os processos da rota get_processing
    """
    def __init__(self, request: RequestProcessing) -> None:
        self._request: RequestProcessing = request
        self.year = request.year
        self.year_as_unique_column = request.year_as_unique_column 
        

    def execute(self) -> pd.DataFrame:
        """
        Executa o processo de busca das informações de Processamento na embrapa

        returns: 
            dataset_production (pd.DataFrame): Dataset com as informações de Processamento
        """
        return processa_usecase(self._request.categoria.__str__(), EnumTabs.processing_tab.__str__(), self.year, self.year_as_unique_column)