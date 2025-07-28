artistas = dbname['artista']
albuns = dbname['album']
gravadoras = dbname['gravadora']


#Insert

artista1 = {
    "Nome": "Dua Lipa",
    "Ano_inicio": 2015,
    "Gravadora": "Warner Bros",
    "Albuns": ["Dua Lipa", "Future Nostalgia", "Radical Optimism"]
}

artistas.insert_many([artista1])
albuns.insert_many([albun1])
gravadoras.insert_many([gravadora1])

#Listar coleção
l_artistas = list(artistas.find())
l_albuns = list(albuns.find())
l_gravadoras = list(gravadoras.find())

pesquisa = {"Nome": ''}

#Find
enc_artista = artistas.find_one(pesquisa)