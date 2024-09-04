from convert_data import converter_nan_para_str_zero, imprimir_linha_e_tipos, converter
import traceback
import os
import pandas as pd
import mysql.connector

def connect_to_db(host, user, password, database):
    #Conecta ao banco de dados e retorna a conexão e o cursor.
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    cursor = conn.cursor()
    return conn, cursor

def verificar_linha(linha):
    #Verifica os tipos de dados de uma linha antes de enviá-la para o banco de dados.    
    
    if linha['produto'] is not None and not isinstance(linha['produto'], int):
        return False
    if linha['foto'] is not None and (not isinstance(linha['foto'], str) or len(linha['foto']) > 100):
        return False
    return True
    

def insert_data_to_db(cursor, df, table_name):
    #Insere dados do DataFrame no banco de dados.
    columns = df.columns.tolist()
    placeholders = ", ".join(["%s"] * len(columns))
    columns_str = ", ".join(columns)
    sql = f"INSERT INTO {table_name} ({columns_str}) VALUES ({placeholders})"
    
    for _, row in df.iterrows():
        if verificar_linha(row):
            values = tuple(row)
            cursor.execute(sql, values)
            print(row)
        else:
            print(f"Dados inválidos encontrados na linha: {row}")

def main():
    # Configurações do banco de dados a partir de variáveis de ambiente
    db_config = {
        'host': os.getenv('DB_HOST', 'default_host'),
        'user': os.getenv('DB_USER', 'default_user'),
        'password': os.getenv('DB_PASSWORD', 'default_password'),
        'database': os.getenv('DB_NAME', 'default_database')
    }
    
    # Nome da tabela no banco de dados
    table_name = 'produtos_imagens' 

    # Conectar ao banco de dados
    conn, cursor = connect_to_db(
        db_config['host'], 
        db_config['user'], 
        db_config['password'], 
        db_config['database']
    )
    
    try:
        # Converter o arquivo Excel   
        df = converter()
        print("Arquivo importado")

        #df = pd.read_excel("produtos_ajustado.xlsx")
        # Inserir dados no banco de dados
        insert_data_to_db(cursor, df, table_name)
        
        # Confirmar as mudanças
        conn.commit()
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        traceback.print_exc()
        conn.rollback()
    finally:
        # Fechar o cursor e a conexão
        cursor.close()
        conn.close()

if __name__ == "__main__":
    main()
