import pandas as pd

def converter_nan_para_str_zero(df):
    # Substituir todos os valores NaN por "0" (como string)
    df = df.fillna("0")
    return df

def imprimir_linha_e_tipos(df):
    # Iterar sobre cada linha do DataFrame
    for i in range(len(df)):
        
        linha_atual = df.iloc[i]
        print(f"Linha {i + 1}:")
        for coluna_nome, valor in linha_atual.items():
            
            tipo_valor = type(valor).__name__
            print(f"  Coluna '{coluna_nome}': Valor = {valor}, Tipo = {tipo_valor}")
            if tipo_valor == 'int64':
                valor = int(valor)
                tipo_valor = type(valor)
                print(f"  Coluna alterada ->>>'{coluna_nome}': Valor = {valor}, Tipo = {tipo_valor}")
        print("-" * 50)

def converter():
    # Exemplo de uso com um arquivo Excel
    data = 'link_imagens_5.xlsx'
    df = pd.read_excel(data)
    
    # Converter NaN para "0"
    df = converter_nan_para_str_zero(df)
    
    # Imprimir as linhas e os tipos após a conversão
    imprimir_linha_e_tipos(df)
    
    return df

# Executar o código
#df_result = converter()
