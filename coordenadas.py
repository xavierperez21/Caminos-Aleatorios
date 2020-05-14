
class Coordenada:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    #Aqui recibimos la nueva distancia en x o y a donde se movera la coordenada del borracho
    def mover(self, delta_x, delta_y):
        return Coordenada(self.x + delta_x, self.y + delta_y)

    #otra coordenada se refiere a la cordenada donde queremos obtener la distancia (el origen generalmente)
    def distancia(self, otra_coordenada):
        delta_x = self.x - otra_coordenada.x
        delta_y = self.y - otra_coordenada.y

        return (delta_x**2 + delta_y**2)**0.5