"""
Todos
30 de junio de 2023
ejemplo
"""

class HuffmanCoding:
    def __init__(self):
        pass

    def encode(self, cadena):
        frecuencia = {}

        for i in cadena:
            if i in frecuencia:
                frecuencia[i] += 1
            else: frecuencia[i] = 1

        return frecuencia

    def getTree(self):
        pass

    def getTable(self):
        pass

    def Summary(self):
        pass
