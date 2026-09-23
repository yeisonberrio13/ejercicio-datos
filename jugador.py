class jugador:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def describir(self):
        return f"{self.nombre} tiene {self.edad} años"


jugador1 = jugador("yeison ", 28)
    