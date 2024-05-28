from node import Node

GENRE_CODES = {
    "Action": 1,
    "Animação": 2,
    "Crime": 3,
    "Drama": 4,
    "Fantasy": 5,
    "Thriller": 6,
}

class MovieNode(Node):
    def __init__(self, title, genre, rating, year):
        super().__init__(year)  # Utilize o ano de lançamento como chave na árvore binária
        self.title = title
        self.genre = genre
        self.rating = rating
        self.year = year
        self.genre_code = GENRE_CODES.get(genre, 0)  # 0 para gêneros não mapeados