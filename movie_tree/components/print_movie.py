from movie_tree.interface.node import Node

class PrintMovie:

    @staticmethod
    def print_tree(root: Node = None, side: str = "") -> None:
        if root is None:
            return
        
        PrintMovie.print_tree(root.left, "l")
        print(root.title, "-", root.genre, "-", root.rating, "-", root.year, "-", root.genre_code, "-", side)
        PrintMovie.print_tree(root.right, "r")


    @staticmethod
    def print_tree_pre(root: Node = None) -> None:
        if root is None:
            return
        
        print(root.title, "-", root.genre, "-", root.rating, "-", root.year)
        PrintMovie.print_tree_pre(root.left)
        PrintMovie.print_tree_pre(root.right)

    @staticmethod
    def print_tree_pos(root: Node = None) -> None:
        if root is None:
            return
        
        PrintMovie.print_tree_pos(root.left)
        PrintMovie.print_tree_pos(root.right)
        print(root.title, "-", root.genre, "-", root.rating, "-", root.year)