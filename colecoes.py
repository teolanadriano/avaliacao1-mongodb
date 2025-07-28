artista = {
    "id": int
    "Nome": str,
    "Ano_inicio": int,
    "Gravadora": 'fk_gravadora',
    "Albums": []
}

album = {
    "id": int,
    "Nome": str
    "Artista": str,
    "Ano": int,
    "Genero": str,
    "Duracao": float,
    "Musicas": []
}

gravadora = {
    "id": int,
    "Nome": str,
    "Pais": str,
    "Contato": '',
    "Artistas": []
}