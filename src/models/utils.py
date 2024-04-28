import re
import requests
import pandas as pd
from bs4 import BeautifulSoup

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
