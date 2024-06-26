# Link para o Projeto Grupo 18: https://github.com/tsujjii/TechChallenge.git

## Visão de Projeto

A ideia é criar um scraper para consumir os dados do site da Embrapa, das seguintes categorias:
* [Produção](http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_02)
* [Processamento](http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_03)
* [Comercialização](http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_04)
* [Importação](http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_05)
* [Exportação](http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_06)

### Definições
**1** - Inicialmente, a API terá as opções para consumir e retornar os dados, ou apenas consumir e armazenar os dados localmente.

**2** - A ideia é criar uma rota (usecase) para cada categoria, assim podendo parametrizar adequadamente para cada categoria. 
Os dados devem ser gerados e salvos como csv, o retorno deve ser um 204 ou o arquivo csv.

### Deploy
Inicialmente o deploy da aplicação foi realizado utilizando a plataforma [Render](https://dashboard.render.com), portanto, já está disponível para que possa ser utilizada e testata neste [link](https://techchallenge-dbkt.onrender.com/docs#/).

![image](https://github.com/tsujjii/TechChallenge/assets/114022011/87570dcb-2c98-4d97-8048-2380e3445703)



### Após clonar o Repositório.

```shell
# Instale o gerenciador de dependencias poetry
pip install poetry

#Inicialize a .venv
poetry shell

#Instale as dependencias do projeto
poetry install
```


### Estrutura do Projeto
~~~~
├── src ----------------------- Pasta Raiz do projeto
│   ├── api ------------------- Responsável por conter os arquivos para subir a API.
│   ├── data ------------------ Armazena dados no formato .parquet, .csv, .xls, etc.
│   ├── models ---------------- Contém arquivos relacionados a modelos e processos.
│   └── usecases -------------- Contém os casos de uso da API.
│       ├── data_production --- Usecase responsável por realizar as tratativas da rota "get_production".
│       └── ... --------------- Outros casos de uso.
├── pyproject.toml ------------ Contém metadados e configurações do projeto, incluindo as dependências gerenciadas pelo Poetry.
├── .gitignore ---------------- Arquivo de configuração do Git para ignorar arquivos específicos.
├── README.md ----------------- Documentação principal do projeto.
└── poetry.lock --------------- Utilizado pelo Poetry para garantir a reprodutibilidade das dependências do projeto.

