from node import Node

class RemoveMovie:
    @staticmethod
    def remove_movie(root: Node = None, field: str = None, value = None):
        if (root is None or field is None or value is None):
            return None

        # Percorre a árvore primeiro (pós-ordem)
        root.left = RemoveMovie.remove_movie(root.left, field, value)
        root.right = RemoveMovie.remove_movie(root.right, field, value)

        # Valor dinâmico do atributo
        current_value = getattr(root, field, None)

        if current_value == value:
            # Caso 1: sem filho esquerdo
            if root.left is None:
                return root.right
            
            # Caso 2: sem filho direito
            if root.right is None:
                return root.left
            
            # Caso 3: dois filhos
            successor = RemoveMovie.min_value_node(root.right)

            # Copiar TODOS os atributos dinamicamente
            for attr, val in vars(successor).items():
                setattr(root, attr, val)

            # Remover o sucessor corretamente
            root.right = RemoveMovie.remove_movie(
                root.right,
                field,
                getattr(successor, field)
            )

        return root
        
    @staticmethod
    def min_value_node(node: Node) -> Node:
        current = node

        # Encontrar o nó mais à esquerda
        while current.left is not None:
            current = current.left
        
        return current