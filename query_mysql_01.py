import mysql.connector
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()
con = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            database=os.getenv('DB_NAME'),
            password=os.getenv('DB_PASSWORD')
)

if con.is_connected():
    db_info = con.get_server_info()
    print(f'Conectado, informações: \n {db_info}')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM produtos ORDER BY id DESC LIMIT 531")
    # Executa a consulta para selecionar os 10 primeiros itens
    #cursor.execute("SELECT * FROM produtos LIMIT 10;")  
    result_set = cursor.fetchall()
    print(f'Conectado, informações: \n {result_set}')

    # Obtenha os nomes das colunas do cursor
    column_names = [x[0] for x in cursor.description]

    # Crie o DataFrame com os resultados e os nomes das colunas
    df = pd.DataFrame(result_set, columns=column_names)

    # Exporte para um arquivo Excel chamado 'resultado.xlsx'
    df.to_excel('resultado.xlsx', index=False)
    print(f'Conectado, informações: \n {result_set}')
else:
    print("Erro")