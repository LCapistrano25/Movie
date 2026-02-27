from node import Node
from .components.add_movie import AddMovie
from .components.remove_movie import RemoveMovie
from .components.search_movie import SearchMovie

class MovieBinaryTree:
    def __init__(self):
        self.root = None

    def add_movie(self, title, genre, rating, year):
        self.root = AddMovie.add_movie(self.root, title, genre, rating, year)

    def search_movies(self, root: Node, field: str, value: str) -> list:
        return SearchMovie.search_movies(root, field, value)

    def recommend_movies(self, root, genre, min_rating, start_year=None, end_year=None):
        if root is None:
            return []

        movies = []
        if root.genre == genre and root.rating >= min_rating:
            if (start_year is None or root.year >= start_year) and (end_year is None or root.year <= end_year):
                movies.append(root.title)

        movies += self.recommend_movies(root.left, genre, min_rating, start_year, end_year)
        movies += self.recommend_movies(root.right, genre, min_rating, start_year, end_year)

        return movies

    def remove_movie(self, root, field: str, value: str):
        RemoveMovie.remove_movie(root, field, value)
        
    def remove_movie_by_genre(self, root, genre):
        RemoveMovie.remove_movie(root, "genre", genre)
        
    def remove_movie_by_title(self, root, title):
        RemoveMovie.remove_movie(root, "title", title)

    def remove_movie_by_rating(self, root, rating):
        RemoveMovie.remove_movie(root, "rating", rating)
