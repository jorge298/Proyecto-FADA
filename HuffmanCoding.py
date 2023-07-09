"""
Todos
30 de junio de 2023
ejemplo
"""

class HuffmanCoding:
    def __init__(self) -> None:
        pass

    def encode(cadena):
        frecuencia = {}

        for i in cadena:
            if i in frecuencia:
                frecuencia[i] += 1
            else: frecuencia[i] = 1

        return frecuencia

    print(encode("mi pasion es programar"))
