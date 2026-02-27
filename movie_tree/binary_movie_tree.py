from components.movie_add import MovieAdd

class MovieBinaryTree:
    def __init__(self):
        self.root = None

    def add_movie(self, title, genre, rating, year):
        self.root = MovieAdd.add_movie(self.root, title, genre, rating, year)
        
    def search_movies_by_title(self, root, title):
        if root is None:
            return None

        if root.title == title:
            return root

        result = self.search_movies_by_title(root.left, title)
        if result:
            return result

        return self.search_movies_by_title(root.right, title)

    def search_movies_by_genre(self, root, genre):
        if root is None:
            return []

        movies = []
        if root.genre == genre:
            movies.append(root)

        movies += self.search_movies_by_genre(root.left, genre)
        movies += self.search_movies_by_genre(root.right, genre)

        return movies

    def search_movies_by_rating(self, root, min_rating):
        if root is None:
            return []

        movies = []
        if root.rating >= min_rating:
            movies.append(f"{root.title} - {root.genre} - {root.rating} - {root.year}")

        movies += self.search_movies_by_rating(root.left, min_rating)
        movies += self.search_movies_by_rating(root.right, min_rating)

        return movies
    
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

    def remove_movie_by_genre(self, root, genre):
        if root is None:
            return None
        
        root.left = self.remove_movie_by_genre(root.left, genre)
        root.right = self.remove_movie_by_genre(root.right, genre)

        if root.genre == genre:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                # Encontrar o sucessor in-order (menor nó na subárvore direita)
                successor = self._min_value_node(root.right)
                
                # Copiar os dados do sucessor para este nó
                root.title = successor.title
                root.genre = successor.genre
                root.rating = successor.rating
                root.year = successor.year
                root.genre_code = successor.genre_code

                # Remover o sucessor
                root.right = self.remove_movie_by_genre(root.right, successor.genre)
        
        return root

    def remove_movie_by_title(self, root, title):
        if root is None:
            return None
        
        root.left = self.remove_movie_by_title(root.left, title)
        root.right = self.remove_movie_by_title(root.right, title)

        if root.title == title:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                # Encontrar o sucessor in-order (menor nó na subárvore direita)
                successor = self._min_value_node(root.right)
                
                # Copiar os dados do sucessor para este nó
                root.title = successor.title
                root.genre = successor.genre
                root.rating = successor.rating
                root.year = successor.year
                root.genre_code = successor.genre_code

                # Remover o sucessor
                root.right = self.remove_movie_by_title(root.right, successor.title)
        
        return root

    def remove_movie_by_rating(self, root, rating):
        if root is None:
            return None
        
        root.left = self.remove_movie_by_rating(root.left, rating)
        root.right = self.remove_movie_by_rating(root.right, rating)

        if root.rating == rating:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                # Encontrar o sucessor in-order (menor nó na subárvore direita)
                successor = self._min_value_node(root.right)
                
                # Copiar os dados do sucessor para este nó
                root.title = successor.title
                root.genre = successor.genre
                root.rating = successor.rating
                root.year = successor.year
                root.genre_code = successor.genre_code

                # Remover o sucessor
                root.right = self.remove_movie_by_rating(root.right, successor.rating)
        
        return root

    def _min_value_node(self, node):
        current = node

        # Encontrar o nó mais à esquerda
        while current.left is not None:
            current = current.left
        
        return current
    
    def print_tree(self, root, side=""):
        if root is None:
            return
        
        self.print_tree(root.left, "l")
        print(root.title, "-", root.genre, "-", root.rating, "-", root.year, "-", root.genre_code, "-", side)
        self.print_tree(root.right, "r")


    def print_tree_pre(self, root):
        if root is None:
            return
        
        print(root.title, "-", root.genre, "-", root.rating, "-", root.year)
        self.print_tree_pre(root.left)
        self.print_tree_pre(root.right)

    def print_tree_pos(self, root):
        if root is None:
            return
        
        self.print_tree_pos(root.left)
        self.print_tree_pos(root.right)
        print(root.title, "-", root.genre, "-", root.rating, "-", root.year)