import requests
import pandas as pd
from bs4 import BeautifulSoup

# Função para obter dados do site
def obter_dados_do_site(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Encontrar a tabela de dados
    tabela = soup.find('table', {'id': 'pokedex'})
    
    # Extrair dados da tabela
    dados_do_site = []
    for row in tabela.find_all('tr')[1:]:  # Ignorar o cabeçalho
        cols = row.find_all(['th', 'td'])
        dados_da_linha = [col.text.strip() for col in cols]
        dados_do_site.append(dados_da_linha)
    
    return dados_do_site

# Função para obter dados da API
def obter_dados_da_api(api_url):
    response = requests.get(api_url)
    dados_da_api = response.json()
    
    return dados_da_api

# Função para agregar os dados e criar um DataFrame
def agregar_dados(dados_site, dados_api):
    # Criar um DataFrame a partir dos dados do site
    df_site = pd.DataFrame(dados_site, columns=['Numero', 'Nome', 'Tipe', 'Total', 'HP', 'Ataque', 'Defesa', 'Velocidade', 'Velocidade de ataque', 'Velocidade de defesa'])
    
    # Criar um DataFrame a partir dos dados da API
    df_api = pd.DataFrame([dados_api])
    
    # Agregar os DataFrames
    dados_agregados_df = pd.concat([df_site, df_api], axis=1)
    
    return dados_agregados_df

# URL do site
url_site = 'https://pokemondb.net/pokedex/all'

# URL da API
url_api = 'https://pokeapi.co/api/v2/pokemon/ditto'

# Obter dados do site
dados_site = obter_dados_do_site(url_site)

# Obter dados da API
dados_api = obter_dados_da_api(url_api)

# Agregar os dados e criar um DataFrame
dados_agregados_df = agregar_dados(dados_site, dados_api)

# Exibir o DataFrame
print(dados_agregados_df)
