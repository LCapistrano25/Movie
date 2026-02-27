from .interface.node import Node
from .components.add_movie import AddMovie
from .components.remove_movie import RemoveMovie
from .components.search_movie import SearchMovie
from .components.recommend_movie import RecommendMovie

class MovieBinaryTree:
    def __init__(self):
        self.root = None

    def add_movie(self, title, genre, rating, year):
        self.root = AddMovie.add_movie(self.root, title, genre, rating, year)

    def search_movies(self, root: Node, field: str, value: str) -> list:
        return SearchMovie.search_movies(root, field, value)

    def recommend_movies(self, root, genre, min_rating, start_year=None, end_year=None):
        return RecommendMovie.recommend_movies(root, genre, min_rating, start_year, end_year)

    def remove_movie(self, root, field: str, value: str):
        RemoveMovie.remove_movie(root, field, value)