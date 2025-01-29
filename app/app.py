import os
import requests
# import dotenv
import pandas as pd

# scope = 'xdr.alr.r xdr.alr.rw xdr.dbr.r xdr.dbr.rw xdr.dp.r xdr.dp.rw xdr.ind.r xdr.ind.rw xdr.org.adm xdr.rul.r xdr.rul.rw xdr.so.r xdr.so.rw xdr.srh.adv xdr.srh.r xdr.srh.rw'

#LADO FIREEYE
def get_saved_searches_f(helix_id, apikey, empresa):
    try:
        url = f"https://apps.fireeye.com/helix/id/{helix_id}/api/v3/search/saved/?limit=100"

        response = requests.get(
            url, 
            headers={
                "accept": "application/json", 
                "x-fireeye-api-key": apikey})

        results = response.json()['results']  
        save_results_to_excel(results, empresa)
        return 'ok'
    except Exception as e:
        print(e)
        return None


# LADO TRELLIX
def get_access_token(client_id, client_secret):
        try:
            url = 'https://auth.trellix.com/auth/realms/IAM/protocol/openid-connect/token'
            response = requests.post(
                url, 
                headers={
                    'Content-Type': 'application/x-www-form-urlencoded'
                }, 
                auth=(client_id, client_secret), 
                data={
                    'grant_type': 'client_credentials',
                    'scope': 'xdr.alr.r xdr.alr.rw xdr.dbr.r xdr.dbr.rw xdr.dp.r xdr.dp.rw xdr.ind.r xdr.ind.rw xdr.org.adm xdr.rul.r xdr.rul.rw xdr.so.r xdr.so.rw xdr.srh.adv xdr.srh.r xdr.srh.rw'
                })
            
            access_token = response.json()['access_token']  
            return access_token
        except Exception as e:
            print(e)
            return None


def get_saved_searches_t(helix_id, access_token, empresa):
    try:
        url = f"https://apps.fireeye.com/helix/id/{helix_id}/api/v3/search/saved/?limit=100"
        
        response = requests.get(
            url, 
            headers={
                "x-trellix-api-token": f"Bearer {access_token}",
                "accept": "application/json"
            })
        results = response.json()['results']  
        save_results_to_excel(results, empresa)
        return 'ok'
    except Exception as e:
        print(e)
        return None


# CRIAR EXCEL
def save_results_to_excel(results, empresa):
    # Filtra apenas os campos 'name' e 'query'
    filtered_results = [{'name': result['name'], 'query': result['query']} for result in results]
    df = pd.DataFrame(filtered_results)  # Cria um DataFrame a partir dos resultados filtrados
    df.to_excel(f'{empresa}.xlsx', index=False)  # Salva o DataFrame em um arquivo XLSX


# menu
def receber_entrada(lado):
    if lado == '1':
        os.system('cls')
        nome_empresa = input("Digite o nome da empresa: ")
        helix_id = input("Digite seu Helix ID: ")
        apikey = input("Digite sua API Key: ")
        get_saved_searches_f(helix_id, apikey, nome_empresa)
        return None
    elif lado == '2':
        os.system('cls')
        nome_empresa = input("Digite o nome da empresa: ")
        helix_id = input("Digite seu Helix ID: ")
        client_id = input("Digite seu Client ID: ")
        client_secret = input("Digite seu Client Secret: ")
        access_token = get_access_token(client_id, client_secret)
        get_saved_searches_t(helix_id, access_token, nome_empresa)
        return None
    else:
        os.system('cls')
        print("Lado inválido. Por favor, escolha '1 - FireEye' ou '2 - Trellix'.")
        return None

# Exemplo de uso
while True:
    try:
        os.system('cls')
        lado = input("Digite o lado (1 - FireEye ou 2 - Trellix) ou '0 - sair' para encerrar: ")
        if lado == '0':
            os.system('cls')
            print('Programa encerrado!')
            break
        dados = receber_entrada(lado)
        if dados:
            os.system('cls')
            print('Dados salvos com sucesso!')
    except KeyboardInterrupt:
        os.system('cls')
        print('Programa encerrado!')
        break














