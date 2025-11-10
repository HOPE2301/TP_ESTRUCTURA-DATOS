class Habilidad:
    def __init__(self,nombre,nivel_habilidad):
        self.nombre = nombre
        self.nivel_habilidad = nivel_habilidad
        #pasamos los niveles de habilidad a un valor numerico:
        aux = {"Principiante": 1, "Intermedio": 2, "Profesional": 3}
        #guardarlo en una variable nivelNum y si no se encuentra el nivel de habilidad devuelva cero:
        self.nivelNum = aux.get(nivel_habilidad, 0) 


    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self,nombre):
        self.nombre = nombre   


    def info(self):
        print (f" {self.nombre} tiene un nivel de habilidad {self.nivel_habilidad}: {self.nivelNum}")
        
class Transformacion(Habilidad):
    def __init__(self, nombre,nivel_habilidad):
        #llamamos al nombre y nivel_habilidad del constructor de Habilidad:
        super().__init__(nombre,nivel_habilidad)
        self.multiplicador = multiplicador
