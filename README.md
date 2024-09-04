# MySQL_Data

Este projeto permite a inserção de dados em um banco de dados MySQL hospedado na HostGator, utilizando Python. O objetivo é automatizar o processo de inserção de dados a partir de um DataFrame do pandas, com verificação de tipos e valores antes da inserção.

## Estrutura do Projeto

O projeto está estruturado da seguinte forma:

- **converter_valor**: Módulo contendo funções auxiliares como `converter_nan_para_str_zero`, `imprimir_linha_e_tipos`, e `converter`.
- **main.py**: Arquivo principal que executa a inserção de dados no banco de dados.
- **requeriments.txt**: Arquivo de dependências necessárias para a execução do projeto.

## Funcionalidades

- Conexão com o banco de dados MySQL utilizando `mysql.connector`.
- Verificação de tipos e valores dos dados antes da inserção.
- Inserção de dados a partir de um DataFrame no banco de dados.
- Tratamento de exceções durante o processo de inserção.

## Requisitos

O projeto utiliza as seguintes bibliotecas Python:

- `mysql-connector-python`: Para a conexão com o banco de dados MySQL.
- `pandas`: Para manipulação de dados em DataFrames.
- `traceback`: Para captura e exibição de exceções.
- `os`: Para trabalhar com variáveis de ambiente.

As dependências podem ser instaladas utilizando o arquivo `requeriments.txt`:
