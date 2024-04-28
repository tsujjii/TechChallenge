from enum import Enum

class EnumProcessing(Enum):
    """
    Enumeração para tipos de processamento de uvas.
    ___
    **Itens:**
    *   viniferas: 1
    *   americanas_hibridas: 2
    *   uvas_mesa: 3
    *   sem_classificacao: 4
    """
    viniferas = 1 
    americanas_hibridas = 2
    uvas_mesa = 3
    sem_classificacao = 4

    def __str__(self):
        return f'subopt_{self.value:02d}'