import os
import pandas as pd

# Carregar o arquivo Excel
df = pd.read_excel(r"C:\Users\inec\Documents\_projetos\freelas\scraping_sites_estevao\site_gruposhopmix\link_imagens.xlsx")

# Definir o caminho da pasta onde as imagens estão armazenadas
pasta_imagens = r'C:\Users\inec\Documents\_projetos\freelas\scraping_sites_estevao\site_gruposhopmix\imagens_capa'

# Função para ajustar o nome do arquivo
def ajustar_nome(nome_imagem):
    if len(nome_imagem) > 100:
        print(len(nome_imagem))
        nome, ext = os.path.splitext(nome_imagem)
        nome = nome[:35] + nome[-(95 - 35 - len(ext)):]  # Manter primeiros 10 e ajustar o final
        
        return nome + ext
    return nome_imagem

# Processar cada linha da planilha
for index, row in df.iterrows():
    id_imagem = row['id']
    if id_imagem =="199830959" or id_imagem == 199830959:
        print("aqui")
    nome_imagem = row['nome_img']  # Ajuste o nome da coluna conforme necessário
    
    caminho_imagem = os.path.join(pasta_imagens, nome_imagem)

    if os.path.exists(caminho_imagem):
        novo_nome = ajustar_nome(nome_imagem)
        novo_caminho = os.path.join(pasta_imagens, novo_nome)
        tamanho_in = 0
        if len(nome_imagem) > 100:
            # Renomear a imagem
            tamanho_in = len(nome_imagem)
            os.rename(caminho_imagem, novo_caminho)        
        # Atualizar o nome na planilha
        df.at[index, 'novo_nome'] = novo_nome
        df.at[index, 'link'] = novo_caminho
        tamanho_at = len(novo_nome)
        #print(caminho_imagem)
        print(f"{tamanho_in} -> {tamanho_at} | {novo_nome}")
# Salvar a planilha atualizada
df.to_excel(r"C:\Users\inec\Documents\_projetos\freelas\scraping_sites_estevao\site_gruposhopmix\link_imagens_3.xlsx", index=False)
