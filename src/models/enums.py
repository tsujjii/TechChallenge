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


class EnumImport(Enum):
    """
    Enumeração para importação de derivados de uva.
    ___
    **Itens:**
    *   vinho_mesa: 1
    *   espumantes: 2
    *   uvas_frescas: 3
    *   uvas_passas: 4
    *   suco_de_uva: 5
    """
    vinho_mesa = 1 
    espumantes = 2
    uvas_frescas = 3
    uvas_passas = 4
    suco_de_uva = 5

    def __str__(self):
        return f'subopt_{self.value:02d}'


class EnumExport(Enum):
    """
    Enumeração para exportação de derivados de uva.
    ___
    **Itens:**
    *   vinho_mesa: 1
    *   espumantes: 2
    *   uvas_frescas: 3
    *   suco_de_uva: 4
    """
    vinho_mesa = 1 
    espumantes = 2
    uvas_frescas = 3
    suco_de_uva = 4

    def __str__(self):
        return f'subopt_{self.value:02d}'


class EnumTabs(Enum):
    """
    Enumeração para as abas disponíveis para mineração.
    ___
    **Itens:**
    *   production_tab: 2
    *   processing_tab: 3
    *   commercialization_tab: 4
    *   import_tab: 5
    *   export_tab: 6
    """
    production_tab = 2
    processing_tab = 3
    commercialization_tab = 4
    import_tab = 5
    export_tab = 6

    def __str__(self):
        return f'opt_{self.value:02d}'
    

class EnumCategoriaDefault(Enum):
    """
    Enumeração default.
    ___
    **Itens:**
    *   default: 1
    """
    default = 1 

    def __str__(self):
        return f'subopt_{self.value:02d}'

