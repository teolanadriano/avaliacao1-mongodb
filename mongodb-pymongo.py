from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pprint import pprint

uri = "mongodb+srv://Teolan:td2312@cluster0.ex49ok1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi('1'))

bancoDeDados = client['sample_mflix']
collection_filmes = bancoDeDados['movies']

query = {"title": "Regeneration"}

try:
    filme = collection_filmes.find_one(query)
    if filme:
        print("Filme encontrado!", filme['title'])
        pprint(filme)
    else:
        print("Nenhum filme encontrado!")

except Exception as e:
    print(f"Erro: {e}")

finally:
    client.close()