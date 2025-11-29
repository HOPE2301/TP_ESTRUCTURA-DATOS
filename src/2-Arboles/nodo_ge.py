class geNodo:
    def __init__(self,datos):
        self.datos = datos
        self.hijos = [] 
        
    def agregar_hijo(self, nodo_hijo):
        self.hijos.append(nodo_hijo) 
