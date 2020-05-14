import random

class Borracho:

    def __init__(self, nombre):
        self.nombre = nombre

#Creamos una segunda clase de borracho, ya que podríamos crear otra que camine mas hacia el sur o hacia el norte, etc.
class BorrachoTradicional(Borracho):

    def __init__(self, nombre):
        super().__init__(nombre)

    #random.choice va a escojer una tupla de la lista aleatoriamente
    def camina(self):
        return random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])    #Las tuplas dentro de la lista representan (x,y)
