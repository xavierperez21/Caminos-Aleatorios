from borrachos import BorrachoTradicional
from campo import Campo
from coordenadas import Coordenada
from bokeh.plotting import figure, show, output_file


def caminata(campo, borracho, pasos):
    inicio = campo.obtener_coordenada(borracho)

    for _ in range(pasos):
        campo.mover_borracho(borracho)

    return inicio.distancia(campo.obtener_coordenada(borracho))



def simular_caminata(pasos, numero_de_intentos, tipo_de_borracho):
    borracho = tipo_de_borracho(nombre='Xavier')    #Inicializamos la instancia de borracho, esta funcion sería como una función agnóstica ya que no le importa el tipo de borracho que sea.
    origen = Coordenada(0,0)
    distancias = []             #Aqui guardaremos las 100 distancias debido a los 100 intentos

    for _ in range(numero_de_intentos):     #El guion bajo quiere decir que no vamos a utilizar la variable iteradora
        campo = Campo()
        campo.anadir_borracho(borracho, origen)
        simulacion_caminata = caminata(campo, borracho, pasos)
        distancias.append(round(simulacion_caminata, 1))

    return distancias



#Graficar estadísticas de acuerdo al numero a cada numero de pasos con los 100 intentos
def graficar(x, y):
    output_file('Caminos_aleatorios.html')
    grafica = figure(title='Camino aleatorio', x_axis_label='pasos', y_axis_label='distancia')
    grafica.line(x, y, legend_label='distancia media')

    show(grafica)



#Graficar los pasos del borracho a manera de ejemplo
def graficar_pasos_borracho(tipo_de_borracho):
    borracho2 = tipo_de_borracho(nombre='Xavi')
    campo2 = Campo()
    origen = Coordenada(0,0)
    campo2.anadir_borracho(borracho2, origen)
    lista_x = []
    lista_y = []
    pasos_del_borracho = 10000

    for _ in range(pasos_del_borracho):
        x, y = campo2.mover_borracho(borracho2, True)
        lista_x.append(x)
        lista_y.append(y)

    output_file('Ejemplo_Caminata_Borracho.html')
    grafica2 = figure(title='Ejemplo Caminata del Borracho')
    grafica2.line(lista_x, lista_y, legend_label='Camino del borracho')

    show(grafica2)



def main(distancias_de_caminata, numero_de_intentos, tipo_de_borracho):
    distancias_media_por_caminata = []

    for pasos in distancias_de_caminata:    #Hacemos una simulacion para 10, luego para 100, luego para 1000, y para 10000
        distancias = simular_caminata(pasos, numero_de_intentos, tipo_de_borracho)
        distancia_media = round(sum(distancias) / len(distancias), 4)
        distancia_maxima = max(distancias)
        distancia_minima = min(distancias)
        distancias_media_por_caminata.append(distancia_media)
        print(f'{tipo_de_borracho.__name__} tuvo una caminata aleatoria de {pasos} pasos')
        print(f'Media = {distancia_media}')
        print(f'Max = {distancia_maxima}')
        print(f'Min = {distancia_minima}')

    graficar(distancias_de_caminata, distancias_media_por_caminata)
    graficar_pasos_borracho(tipo_de_borracho)



if __name__ == "__main__":
    distancias_de_caminata = [10, 100, 1000, 10000]     #Diferentes numeros de pasos que va a recorrer el borracho en cada simulación
    numero_de_intentos = 100 #Para ver en cada simulacion el resultado y obtener una media de todos los resultados

    main(distancias_de_caminata, numero_de_intentos, BorrachoTradicional)