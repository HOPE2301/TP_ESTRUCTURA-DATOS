class Habilidad:
    def __init__(self,nombre,nivel_habilidad):
        self.nombre = nombre
        aux = {"Principiante": 1, "Intermedio": 2, "Profesional": 3}
        self.nivelNum = aux.get(nivel_habilidad, 0)


    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self,nombre):
        self.nombre = nombre   


    def get_nivel_habilidad(self):
        return self.nivel_habilidad
    
    def set_nivel_habilidad(self,nivel_habilidad):
        self.nivel_habilidad = nivel_habilidad

    def info(self):
        print (f" {self.nombre} tiene un nivel de habilidad de: {self.nivel_habilidad}")
        
class transformacion(Habilidad):
    def __init__(self, nombre, multiplicador):
        super().__init__(nombre, multiplicador)
        self.multiplicador = multiplicador