import re
import pandas as pd
from .dtos import RequestProduction
from ...models.utils import processa_usecase
from ...models.enums import EnumTabs, EnumCategoriaDefault

class ProductionUsecase():
    """
    Classe responsável por executar os processos da rota get_production
    """
    def __init__(self, request: RequestProduction) -> None:
        self._request: RequestProduction = request
        self.year = request.year
        self.year_as_unique_column = request.year_as_unique_column 
        

    def execute(self) -> pd.DataFrame:
        """
        Executa o processo de busca das informações de produção na embrapa

        returns: 
            dataset_production (pd.DataFrame): Dataset com as informações de Produção
        """
        return processa_usecase(EnumCategoriaDefault.default.__str__(), EnumTabs.production_tab.__str__(), self.year, self.year_as_unique_column)
