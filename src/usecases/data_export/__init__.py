import re
import pandas as pd
from .dtos import RequestExport
from ...models.enums import EnumTabs
from ...models.utils import processa_usecase_import_export

class ExportUsecase():
    """
    Classe responsável por executar os processos da rota get_import
    """
    def __init__(self, request: RequestExport) -> None:
        self._request: RequestExport = request
        self.year = request.year

    def execute(self) -> pd.DataFrame:
        """
        Executa o processo de busca das informações de Processamento na embrapa

        returns: 
            dataset_production (pd.DataFrame): Dataset com as informações de Processamento
        """
        return processa_usecase_import_export(self._request.categoria.__str__(), EnumTabs.export_tab.__str__(), self.year)