class BiNodo:
    def __init__(self, data):
        self.data = data
        self.izquierdo = None
        self.derecho = None
        
    def agregar(self, data):
        if data.calcular_poder() < self.data.calcular_poder(): 
            if self.izquierdo is None:
                self.izquierdo = BiNodo(data)
            else:
                self.izquierdo.agregar(data)
        else:
            if self.derecho is None:
                self.derecho = BiNodo(data)
            else:
                self.derecho.agregar(data)
    
