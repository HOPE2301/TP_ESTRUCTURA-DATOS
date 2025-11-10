## Recibimos una lista de Planetas, con sus distancias entre sí y devolvemos la ruta mas optimizada usando Dijkstra.
## NOTA: En el grafo se deben informar las distancias entre todos los planetas conectados directamente.
## No usaremos librerías externas para el algoritmo de Dijkstra.

class Planeta:
    def __init__(self, nombre, alianza=None):
        '''
        Clase Planeta.
        Recibimos: nombre --> string, alianza --> string (opcional)
        '''
        self.nombre = nombre
        self.Alianza = alianza  # Alianza a la que pertenece el planeta
        self.conexiones = {}  # Diccionario para almacenar conexiones y sus distancias

    def agregar_conexion(self, otro_planeta, distancia):
        self.conexiones[otro_planeta] = distancia
    
    def obtener_conexiones(self):
        return self.conexiones

    def __str__(self):
        return self.nombre
    
def dijkstra(planetas, inicio, fin,):
    '''
    Dijkstra para encontrar la ruta mas optima entre 2 planetas.
    Recibimos: lista de planetas, planeta de inicio y planeta de fin.
    Planetas son objetos de clase Planeta, Inicio y fin son origen y destino de nuestro viaje
    '''
    distancias = {} ## Distancia entre planetas
    previos = {} ## ya visitamos
    no_visitados = planetas ## planetas no visitados (empezamos con todos)

    ## lo haremos de forma recursiva
    for planeta in planetas:
        distancias[planeta] = float('inf') ## inicializamos todas las distancias como infinitas
        previos[planeta] = None ## inicializamos todos los previos como None
    distancias[inicio] = 0 ## la distancia al planeta de inicio es 0

    while no_visitados:
        ## empezamos el viaje, buscando planetas cercanos...
        planeta_actual = min(no_visitados, key=lambda planeta: distancias[planeta])

        ## si llegamos al planeta de destino hemos finalizado
        if planeta_actual == fin:
            break
        ## si no es el de destino, sigamos...
        no_visitados.remove(planeta_actual) ## ya te visitamos, borramos del checklist

        for vecino, distancia in planeta_actual.obtener_conexiones().items(): ## obtenemos las conexiones del planeta actual
            if vecino in no_visitados: 
                if vecino.Alianza != planeta_actual.Alianza: ## solo si son de alianzas diferentes
                    distancia = distancia * 1.25 ## es mas costoso ir a otras alianzas
                nueva_distancia = distancias[planeta_actual] + distancia ## sumar las distancias
                if nueva_distancia < distancias[vecino]: ## si es mas optima que la ya guardada, usamos esa
                    distancias[vecino] = nueva_distancia ## update de distancia
                    previos[vecino] = planeta_actual ## guardar para poder reconstruir la ruta despues
    ## reconstruimos la ruta
    ruta = []
    actual = fin ## camino inverso
    while actual is not None:
        ruta.append(actual)
        actual = previos[actual]
    ruta.reverse() ## la ponemos de nuevo en orden.
    return ruta, distancias[fin] ## devolvemos la ruta y la distancia total

