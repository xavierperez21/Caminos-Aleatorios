
class Campo:

    def __init__(self):
        self.coordenadas_de_borrachos = {}  #Diccionario que tendra la forma {Borracho1:coordenada, Borracho2:coordenada}

    def anadir_borracho(self, borracho, coordenada):
        self.coordenadas_de_borrachos[borracho] = coordenada

    def mover_borracho(self, borracho, graficar_camino=False):
        delta_x, delta_y = borracho.camina()
        coordenada_actual = self.coordenadas_de_borrachos[borracho]
        nueva_coordenada = coordenada_actual.mover(delta_x, delta_y)

        self.coordenadas_de_borrachos[borracho] = nueva_coordenada

        if graficar_camino == True:
            return (nueva_coordenada.x, nueva_coordenada.y) #new

    def obtener_coordenada(self, borracho):
        return self.coordenadas_de_borrachos[borracho]

