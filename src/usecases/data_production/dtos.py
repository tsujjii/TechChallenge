from pydantic import BaseModel, Field
from typing import Union, List

class RequestProduction(BaseModel):
    """
    Classe responsável por definir os parâmetros de request da rota get_production
    """
    year: Union[Union[List[int], int], None] = Field(title='Ano', description='Ano dos dados a serem retornados', default=None)
    year_as_unique_column: bool = Field(title='Tipo Ano', description='Se informado True, o ano será retornado como uma coluna unificada', default=False)