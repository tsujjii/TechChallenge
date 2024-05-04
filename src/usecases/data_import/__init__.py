import re
import pandas as pd
from .dtos import RequestImport
from ...models.enums import EnumTabs
from ...models.utils import processa_usecase_import_export

class ImportUsecase():
    """
    Classe responsável por executar os processos da rota get_import
    """
    def __init__(self, request: RequestImport) -> None:
        self._request: RequestImport = request
        self.year = request.year

    def execute(self) -> pd.DataFrame:
        """
        Executa o processo de busca das informações de Processamento na embrapa

        returns: 
            dataset_production (pd.DataFrame): Dataset com as informações de Processamento
        """
        return processa_usecase_import_export(self._request.categoria.__str__(), EnumTabs.import_tab.__str__(), self.year)