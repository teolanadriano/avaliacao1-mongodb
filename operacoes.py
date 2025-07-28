artistas = dbname['artista']
albums = dbname['album']
gravadoras = dbname['gravadora']



artistas.insert_many([artista1])
albums.insert_many([album1])
gravadoras.insert_many([gravadora1])

l_artistas = list(artistas.find())
l_albums = list(albums.find())
l_gravadoras = list(gravadoras.find())