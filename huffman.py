"""
Todos
30 de junio de 2023
ejemplo
"""

class HuffmanBinaryTree:
    def __init__(self, key, left, right) -> None:
        self.key = key
        self.left = left
        self.right = right

    def getNumberKey(self):
        if isinstance(self.key, int):
            return self.key
        else: -1

    def getLeft(self):
        pass

    def getRight(self):
        pass
