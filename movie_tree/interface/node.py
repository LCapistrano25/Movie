from abc import ABC
class Node(ABC):
    def __init__(self, content):
        self.content = content
        self.left = None
        self.right = None
