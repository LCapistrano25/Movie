from movie_tree.interface.node import Node

class RecommendMovie:

    @staticmethod
    def recommend_movies(root: Node, genre: str, min_rating: float, start_year: int = None, end_year: int = None):
        if root is None:
            return []
            
        movies = []
        if root.genre == genre and root.rating >= min_rating:
            if (start_year is None or root.year >= start_year) and (end_year is None or root.year <= end_year):
                movies.append(root.title)

        movies += RecommendMovie.recommend_movies(root.left, genre, min_rating, start_year, end_year)
        movies += RecommendMovie.recommend_movies(root.right, genre, min_rating, start_year, end_year)

        return movies