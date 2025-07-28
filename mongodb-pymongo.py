from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pprint import pprint

uri = "mongodb+srv://Teolan:td2312@cluster0.ex49ok1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi('1'))

db = client['Avaliacao']

artistas = db["Artistas"]
albuns = db["Albuns"]
gravadora = db["Gravadoras"]

bancoDeDados = client['sample_mflix']
collection_filmes = bancoDeDados['movies']

client.close()