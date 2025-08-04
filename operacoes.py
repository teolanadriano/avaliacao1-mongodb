from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pprint import pprint

uri = "mongodb+srv://Teolan:td2312@cluster0.ex49ok1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi('1'))

db = client['AAG']

artistas = db['artista']
#albuns = db['album']
#gravadoras = db['gravadora']


#Insert

artista1 = {
    "Nome": "Dua Lipa",
    "Ano_inicio": 2015,
    "Gravadora": "Warner Music Group",
    "Albuns": ["Dua Lipa", "Future Nostalgia", "Radical Optimism"]
}

artista2 = {
    "Nome":
    "Ano_inicio":
    "Gravadora":
    "Albuns": []
}

#artistas.insert_many([artista1])
#albuns.insert_many([albun1])
#gravadoras.insert_many([gravadora1])

#Listar coleção
l_artistas = list(artistas.find())
#l_albuns = list(albuns.find())
#l_gravadoras = list(gravadoras.find())


#Find
pesquisa = {"Nome": 'Dua Lipa'}

#Find
enc_artista = artistas.find_one(pesquisa)
print(enc_artista)