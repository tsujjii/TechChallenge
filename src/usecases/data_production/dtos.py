from pydantic import BaseModel, Field
from typing import Union, List

class RequestProduction(BaseModel):
    """
    Classe responsável por definir os parâmetros de request da rota get_production
    """
    year: Union[List[int], int, None, str] = Field(title='Ano', description='Ano dos dados a serem retornados', default=1970)
    year_as_unique_column: bool = Field(title='Tipo Ano', description='Se informado True, o ano será retornado como uma coluna unificada', default=False)
    save_dataset_localy: bool = Field(title='Salvar dataset', description='Indica se deve salvar o dataset localmente na API', default=False)