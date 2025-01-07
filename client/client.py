import requests

# Configuração do servidor
server_url = "http://localhost:52021/api/recommend"

# Músicas de exemplo para recomendação
# user_songs = ["HUMBLE.", "DNA."]
user_input = input("Digite as músicas que deseja receber recomendações (separadas por vírgula): ")
user_songs = [song.strip() for song in user_input.split(",")]

# Enviar requisição POST
response = requests.post(server_url, json={"songs": user_songs})

# Exibir a resposta
if response.status_code == 200:
    recommendations = response.json()
    print("Recomendações:")
    print(recommendations)
else:
    print(f"Erro: {response.status_code}")
