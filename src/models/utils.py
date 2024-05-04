import re
import requests
import pandas as pd
from bs4 import BeautifulSoup
from typing import Union, List

def scrape_table(url: str, year: int):
    """Função responsável por realizar a busca na url Indicada, minerando os dados da tabela

    parameters:
        url (str): Url para realizar a mineração
        year (int): Ano do dado
    
    returns: 
        df_items (pd.DataFrame): Dataframe com os dados minerados
    """

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table', class_='tb_base tb_dados')

        if table:
            items = []
            sub_items = []
            rows = table.find('tbody').find_all('tr')

            for row in rows:
                cells = row.find_all('td')
                produto = cells[0].text.strip()
                classe = cells[0].get('class')[0] 
                qtd = re.sub(r'\D', '', cells[1].text.strip())
                quantidade = 0 if not qtd else qtd

                if classe == 'tb_item':
                    categoria = produto
                elif classe == 'tb_subitem':
                    sub_items.append((categoria, produto, quantidade))

            df_items = pd.DataFrame(sub_items, columns=['categoria', 'item', 'quantidade'])
            df_items['ano'] = year
            return df_items


def processa_usecase(categoria: str, opcao: str, year_param, year_as_unique_column: bool):
    """Função responsável por realizar as tratativas necessárias para realizar a mineranção dos dados da aba

    parameters:
        categoria (str): categoria que deve ser minerada
        opcao (str): define qual aba será minerada
        year_param (Union[Union[List[int], int]): Ano do dado
        year_as_unique_column: (bool) Define se o ano será retornado como uma coluna única
    
    returns: 
        df_items (pd.DataFrame): Dataframe com os dados minerados
    """
    dfs = []
    if isinstance(year_param, list):
        for year in year_param:
            dfs.append(scrape_table(f'http://vitibrasil.cnpuv.embrapa.br/index.php?ano={year}&opcao={opcao}&subopcao={categoria}', year))
        dataset_production = pd.concat(dfs)
    elif isinstance(year_param, str):
        range_year = [int(match) for match in re.findall(r'\b\d{4}\b', year_param)]
        range_year.sort()
        if isinstance(range_year, list):
            for year in range(range_year[0], (range_year[-1] + 1)):
                dfs.append(scrape_table(f'http://vitibrasil.cnpuv.embrapa.br/index.php?ano={year}&opcao={opcao}&subopcao={categoria}', year))
            dataset_production = pd.concat(dfs)   
    else: 
        try: 
            dataset_production = scrape_table(f'http://vitibrasil.cnpuv.embrapa.br/index.php?ano={year_param}&opcao={opcao}&subopcao={categoria}', year_param)
        except Exception as ex: 
            raise Exception(f"Não foi possível realizar a sua requisição, verifique os parametros informados: {ex}")

    dataset_production = __trata_response_dataset(year_as_unique_column, dataset_production)
    del dfs
    return dataset_production

def __trata_response_dataset(year_as_unique_column: bool, df_tratado: pd.DataFrame) -> pd.DataFrame:
    """
    Trata o dataset para retorar o ano da forma desejada

    parameters:
        df (pd.DataFrame): Dataset a ser organizado

    returns:
        df_tratado (pd.DataFrame): Dataset organizado da forma desejada
    """
    if year_as_unique_column:
        df_tratado = df_tratado.pivot(index=['categoria', 'item'], columns='ano', values='quantidade').reset_index()
        df_tratado.reset_index(drop=True, inplace=True)
    return df_tratado

def scrape_table_import_export(url: str, year: int):
    """Função responsável por realizar a busca na url Indicada, minerando os dados da tabela
        * Função deve somente ser utilizada para as abas de importação e exportação

    parameters:
        url (str): Url para realizar a mineração
        year (int): Ano do dado
    
    returns: 
        df_items (pd.DataFrame): Dataframe com os dados minerados
    """

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table', class_='tb_base tb_dados')

        if table:
            items = []
            sub_items = []
            rows = table.find('tbody').find_all('tr')

            for row in rows:
                cells = row.find_all('td')
                pais = cells[0].text.strip()

                qtd = re.sub(r'\D', '', cells[1].text.strip())
                quantidade = 0 if not qtd else qtd

                vlr = re.sub(r'\D', '', cells[2].text.strip())
                valor = 0 if not vlr else vlr

                sub_items.append((pais, quantidade, valor))

            df_items = pd.DataFrame(sub_items, columns=['pais', 'quantidade', 'valor'])
            df_items['ano'] = year
            return df_items

def processa_usecase_import_export(categoria: str, opcao: str, year_param):
    """Função responsável por realizar as tratativas necessárias para realizar a mineranção dos dados da aba
        * Função deve somente ser utilizada para as abas de importação e exportação

    parameters:
        categoria (str): categoria que deve ser minerada
        opcao (str): define qual aba será minerada
        year_param (Union[Union[List[int], int]): Ano do dado
        year_as_unique_column: (bool) Define se o ano será retornado como uma coluna única
    
    returns: 
        df_items (pd.DataFrame): Dataframe com os dados minerados
    """
    dfs = []
    if isinstance(year_param, list):
        for year in year_param:
            dfs.append(scrape_table_import_export(f'http://vitibrasil.cnpuv.embrapa.br/index.php?ano={year}&opcao={opcao}&subopcao={categoria}', year))
        dataset_production = pd.concat(dfs)
    elif isinstance(year_param, str):
        range_year = [int(match) for match in re.findall(r'\b\d{4}\b', year_param)]
        range_year.sort()
        if isinstance(range_year, list):
            for year in range(range_year[0], (range_year[-1] + 1)):
                dfs.append(scrape_table_import_export(f'http://vitibrasil.cnpuv.embrapa.br/index.php?ano={year}&opcao={opcao}&subopcao={categoria}', year))
            dataset_production = pd.concat(dfs)   
    else: 
        try: 
            dataset_production = scrape_table_import_export(f'http://vitibrasil.cnpuv.embrapa.br/index.php?ano={year_param}&opcao={opcao}&subopcao={categoria}', year_param)
        except Exception as ex: 
            raise Exception(f"Não foi possível realizar a sua requisição, verifique os parametros informados: {ex}")

    del dfs
    return dataset_production