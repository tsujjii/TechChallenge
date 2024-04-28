import re
import pandas as pd
from .dtos import RequestProcessing
from ...models.utils import scrape_table

class ProcessingUsecase():
    """
    Classe responsável por executar os processos da rota get_processing
    """
    def __init__(self, request: RequestProcessing) -> None:
        self._request: RequestProcessing = request
        self.year = request.year if isinstance(request.year, list) else [request.year]
        self.year_as_unique_column = request.year_as_unique_column 
        

    def execute(self) -> pd.DataFrame:
        """
        Executa o processo de busca das informações de Processamento na embrapa

        returns: 
            dataset_production (pd.DataFrame): Dataset com as informações de Processamento
        """

        dfs = []
        if isinstance(self._request.year, list):
            for year in self._request.year:
                dfs.append(scrape_table(f'http://vitibrasil.cnpuv.embrapa.br/index.php?ano={year}&opcao=opt_03&subopcao={self._request.categoria.__str__()}', year))
            dataset_production = pd.concat(dfs)
        elif isinstance(self._request.year, str):
            range_year = [int(match) for match in re.findall(r'\b\d{4}\b', self._request.year)]
            range_year.sort()
            if isinstance(range_year, list):
                for year in range(range_year[0], (range_year[-1] + 1)):
                    dfs.append(scrape_table(f'http://vitibrasil.cnpuv.embrapa.br/index.php?ano={year}&opcao=opt_03&subopcao={self._request.categoria.__str__()}', year))
                dataset_production = pd.concat(dfs)   
        else: 
            try: 
                dataset_production = scrape_table(f'http://vitibrasil.cnpuv.embrapa.br/index.php?ano={self._request.year}&opcao=opt_03&subopcao={self._request.categoria.__str__()}', self._request.year)
            except Exception as ex: 
                raise Exception(f"Não foi possível realizar a sua requisição, verifique os parametros informados: {ex}")

        #TODO Validar se o dataset de resposta está vazio
        dataset_production = self.__trata_response_dataset(dataset_production)
        del dfs
        return dataset_production

    def __trata_response_dataset(self, df_tratado: pd.DataFrame) -> pd.DataFrame:
        """
        Trata o dataset para retorar o ano da forma desejada

        parameters:
            df (pd.DataFrame): Dataset a ser organizado

        returns:
            df_tratado (pd.DataFrame): Dataset organizado da forma desejada
        """
        if self.year_as_unique_column:
            df_tratado = df_tratado.pivot(index=['categoria', 'item'], columns='ano', values='quantidade').reset_index()
            df_tratado.reset_index(drop=True, inplace=True)
        return df_tratado