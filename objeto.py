class Objeto:
    def __init__(self,nombre,nivel_poder):
        self.nombre = nombre
        self.nivel_poder = nivel_poder

    def get_nombre (self):
        return self.nombre
    
    def set_nombre(self,nombre):
        self.nombre = nombre

    def get_nivel_poder(self):
        return self.nivel_poder
    
    def set_nivel_poder(self,nivel_poder):
        self.nivel_poder = nivel_poder

    def informacion(self):
        print (f" el objeto {self.nombre} tiene un nivel de poder de: {self.get_nivel_poder}")
