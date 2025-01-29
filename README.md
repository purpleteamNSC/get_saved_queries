# Projeto de Integração FireEye e Trellix

Este projeto é um script Python que permite a integração com as APIs da FireEye e Trellix para buscar e salvar pesquisas salvas em um arquivo Excel.

## Funcionalidades

- **Obter Pesquisas Salvas da FireEye**: Permite que o usuário insira seu Helix ID e API Key para recuperar pesquisas salvas.
- **Obter Pesquisas Salvas da Trellix**: Permite que o usuário insira seu Helix ID, Client ID e Client Secret para recuperar pesquisas salvas.
- **Salvar Resultados em Excel**: Os resultados das pesquisas são filtrados e salvos em um arquivo Excel.

## Pré-requisitos

Antes de executar o script, você precisa ter o Python instalado em sua máquina. Além disso, você deve instalar as seguintes bibliotecas:

```bash
pip install requests pandas openpyxl
```

## Como Usar

1. Clone este repositório ou baixe o arquivo `app.py`.
2. Abra um terminal e navegue até o diretório onde o arquivo `app.py` está localizado.
3. Execute o script com o seguinte comando:

   ```bash
   python app.py
   ```

4. Siga as instruções no terminal para escolher entre FireEye ou Trellix e insira as credenciais necessárias.

## Estrutura do Código

- `get_saved_searches_f(helix_id, apikey, empresa)`: Obtém pesquisas salvas da FireEye.
- `get_access_token(client_id, client_secret)`: Obtém um token de acesso da Trellix.
- `get_saved_searches_t(helix_id, access_token, empresa)`: Obtém pesquisas salvas da Trellix.
- `save_results_to_excel(results, empresa)`: Salva os resultados em um arquivo Excel.
- `receber_entrada(lado)`: Recebe a entrada do usuário para determinar qual API usar.

## Contribuição

Sinta-se à vontade para contribuir com melhorias ou correções. Para isso, faça um fork do repositório e envie um pull request.

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
