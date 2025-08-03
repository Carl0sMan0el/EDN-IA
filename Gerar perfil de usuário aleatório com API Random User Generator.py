import requests

def gerar_usuario():
    url = "https://randomuser.me/api/"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        usuario = dados['results'][0]
        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']
        print(f"Nome: {nome}\nEmail: {email}\nPaís: {pais}")
    else:
        print("Erro ao acessar a API.")

gerar_usuario()
