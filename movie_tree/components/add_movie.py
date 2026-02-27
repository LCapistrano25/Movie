from interface.node import Node

class AddMovie:
    
    @staticmethod
    def add_movie(root: Node, title: str, genre: str, rating: float, year: int):
        new_movie = Node(title, genre, rating, year)
        root = AddMovie._insert(root, new_movie)
        return root
    
    @staticmethod
    def _insert(root: Node = None, new_movie: Node = None):
        if root is None:
            return new_movie

        if root.year > new_movie.year:
            root.left = AddMovie._insert(root.left, new_movie)
        elif root.year < new_movie.year:
            root.right = AddMovie._insert(root.right, new_movie)
        else:
            # Em caso de anos iguais, comparar por código de gênero
            if root.genre_code > new_movie.genre_code:
                root.left = AddMovie._insert(root.left, new_movie)
            elif root.genre_code < new_movie.genre_code:
                root.right = AddMovie._insert(root.right, new_movie)
            else:
                # Em caso de gênero e ano iguais, comparar por classificação
                if root.rating > new_movie.rating:
                    root.left = AddMovie._insert(root.left, new_movie)
                else:
                    root.right = AddMovie._insert(root.right, new_movie)
        return root