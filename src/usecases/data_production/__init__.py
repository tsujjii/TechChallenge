from .dtos import RequestProduction
import requests, io
import pandas as pd

class ProductionUsecase():
    """
    Classe responsável por executar os processos da rota get_production
    """
    def __init__(self, request: RequestProduction) -> None:
        self.year = request.year if isinstance(request.year, list) else [request.year]
        self.year_as_unique_column = request.year_as_unique_column 
        

    def execute(self) -> pd.DataFrame:
        """
        Executa o processo de busca das informações de produção na embrapa

        returns: 
            dataset_production (pd.DataFrame): Dataset com as informações de Produção
        """
        response = requests.get('http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv')
        if response.status_code == 200:
            df = pd.read_csv(io.StringIO(response.text), sep=";", encoding="utf-8")
        else:
            raise Exception(f"Falha ao conectar com o site: {response.status_code} \n {response.content}")
        
        dataset_production = self.__trata_response_dataset(df)
        del df, response
        return dataset_production

    def __trata_response_dataset(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Trata o dataset para filtrar as informações necessárias e retorna da forma desejada

        parameters:
            df (pd.DataFrame): Dataset a ser filtrado

        returns:
            df_tratado (pd.DataFrame): Dataset filtrado e organizado da forma desejada
        """
        if self.year_as_unique_column:
            df_tratado = df.melt(id_vars=['id', 'produto'], var_name='ano', value_name='valor').drop(columns='id')
            df_tratado['ano'] = df_tratado['ano'].astype(int)
            df_tratado['valor'] = df_tratado['valor'].astype(float)
            if not None in self.year:
                df_tratado = df_tratado[df_tratado['ano'].isin(self.year)]
        else:
            df_tratado = df
            if not None in self.year:
                columns = ['produto'] + [str(year) for year in self.year]
                df_tratado = df_tratado[columns]
            
        del df    
        return df_tratado.reset_index(drop=True)