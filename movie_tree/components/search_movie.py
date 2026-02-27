from movie_tree.interface.node import Node
 
class SearchMovie:
    @staticmethod
    def search_movies(root: Node, field: str, value: str) -> list:
        if root is None:
            return []

        movies = []
        if getattr(root, field) == value:
            movies.append(root)

        movies += SearchMovie.search_movies(root.left, field, value)
        movies += SearchMovie.search_movies(root.right, field, value)

        return movies