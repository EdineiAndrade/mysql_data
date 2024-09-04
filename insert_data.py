from convert_data import converter_nan_para_str_zero, imprimir_linha_e_tipos, converter
import traceback
import os
import pandas as pd
import mysql.connector

def connect_to_db(host, user, password, database):
    """Conecta ao banco de dados e retorna a conexão e o cursor."""
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    cursor = conn.cursor()
    return conn, cursor

def verificar_linha(linha):
    """ Verifica os tipos de dados de uma linha antes de enviá-la para o banco de dados.    
        :param linha: Série representando uma linha do DataFrame.
        :return: True se todos os dados estiverem corretos, senão False.
    """
    if linha['nome'] is not None and (not isinstance(linha['nome'], str) or len(linha['nome']) > 100):
        return False
    if linha['valor'] is not None and not isinstance(linha['valor'], (float, int)):
        return False
    if linha['valor_promo'] is not None and not isinstance(linha['valor_promo'], (float, int)):
        return False
    if linha['estoque'] is not None and not isinstance(linha['estoque'], int):
        return False
    if linha['nivel'] is not None and not isinstance(linha['nivel'], int):
        return False
    if linha['categoria'] is not None and not isinstance(linha['categoria'], int):
        return False
    if linha['subcategoria'] is not None and not isinstance(linha['subcategoria'], int):        
        return False
    if linha['envio'] is not None and (not isinstance(linha['envio'], str) or len(linha['envio']) > 50):
        return False
    if linha['frete'] is not None and not isinstance(linha['frete'], (float, int)):
        return False
    if linha['promocao'] is not None and (not isinstance(linha['promocao'], str) or len(linha['promocao']) > 5):
        return False
    if linha['imagem'] is not None and (not isinstance(linha['imagem'], str) or len(linha['imagem']) > 100):
        return False
    if linha['marca'] is not None and (not isinstance(linha['marca'], str) or len(linha['marca']) > 100):
        return False
    if linha['modelo'] is not None and (not isinstance(linha['modelo'], str) or len(linha['modelo']) > 100):
        return False
    if linha['loja'] is not None and not isinstance(linha['loja'], int):
        return False
    if linha['peso'] is not None and not isinstance(linha['peso'], (float, int)):
        return False
    if linha['descricao'] is not None and not isinstance(linha['descricao'], str):
        return False                                         
    if linha['envio'] is not None and (not isinstance(linha['envio'], str) or len(linha['envio']) > 50):
        return False
    if linha['carac'] is not None and (not isinstance(linha['carac'], str) or len(linha['carac']) > 100):
        return False 
    if linha['nota'] is not None and not isinstance(linha['nota'], int) or (linha['nota']) > 11:
        return False
    if linha['video'] is not None and (not isinstance(linha['video'], str) or len(linha['video']) > 100):
        return False
    if linha['nome_frete'] is not None and (not isinstance(linha['nome_frete'], str) or len(linha['nome_frete']) > 50):
        return False
    if linha['id_fornecedor'] is not None and not isinstance(linha['id_fornecedor'], int) or linha['id_fornecedor'] > 11:
        return False
    if linha['id_produto'] is not None and not isinstance(linha['id_produto'], int):
        return False
    if linha['valor_custo'] is not None and not isinstance(linha['valor_custo'], (float, int)):
        return False
    if linha['largura'] is not None and not isinstance(linha['largura'], int) or linha['largura'] > 11:
        return False
    if linha['altura'] is not None and not isinstance(linha['altura'], int):
        return False
    if linha['comprimento'] is not None and not isinstance(linha['comprimento'], int):
        return False
    if linha['palavras'] is not None and (not isinstance(linha['palavras'], str) or len(linha['palavras']) > 255):
        return False
    
    return True
    

def insert_data_to_db(cursor, df, table_name):
    """Insere dados do DataFrame no banco de dados."""
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
    table_name = 'produtos'  

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
