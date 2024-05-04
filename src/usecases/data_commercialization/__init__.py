import pandas as pd
from .dtos import RequestCommercialization
from ...models.utils import processa_usecase
from ...models.enums import EnumTabs, EnumCategoriaDefault

class CommercializationUsecase():
    """
    Classe responsável por executar os processos da rota get_commercialization
    """
    def __init__(self, request: RequestCommercialization) -> None:
        self._request: RequestCommercialization = request
        self.year = request.year
        self.year_as_unique_column = request.year_as_unique_column 
        
    def execute(self) -> pd.DataFrame:
        """
        Executa o processo de busca das informações de Processamento na embrapa

        returns: 
            dataset_production (pd.DataFrame): Dataset com as informações de Processamento
        """
        return processa_usecase(EnumCategoriaDefault.default.__str__(), EnumTabs.commercialization_tab.__str__(), self.year, self.year_as_unique_column)
