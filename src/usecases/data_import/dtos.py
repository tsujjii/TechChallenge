from typing import Union, List
from pydantic import BaseModel, Field
from ...models.enums import EnumImport

class RequestImport(BaseModel):
    """
    Classe responsável por definir os parâmetros de request da rota get_import
    """
    categoria: EnumImport = Field(title='Categoria', description='Categoria dos dados', default=EnumImport(1))
    year: Union[Union[List[int], int], Union[None, str]] = Field(title='Ano', description='Ano dos dados a serem retornados', default=1970)
    save_dataset_localy: bool = Field(title='Salvar dataset', description='Indica se deve salvar o dataset localmente na API', default=False)