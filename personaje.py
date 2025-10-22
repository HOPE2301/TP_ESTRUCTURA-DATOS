class Personaje:
    def __init__(self,nombre,especie,planeta):
        self.nombre = nombre
        self.especie = especie
        self.planeta = planeta
        self.habilidad = []
        self.inventario = []
        self.total_poder = 0

    def get_nombre (self):
        return self.nombre
    
    def set_nombre(self,nombre):
        self.nombre = nombre

    def get_especie(self):
        return self.especie
    
    def set_especie(self,especie):
        self.especie = especie

    def get_planeta(self):
        return self.planeta
    
    def set_planeta(self,planeta):
        self.planeta = planeta

    def agregar_habilidad(self,habilidad):
        if habilidad in self.habilidad:
            return f"esta habilidad ya se encuentra!"
        else:
            self.habilidad.append(habilidad)
            return f"habilidad agregada"
        
    def quitar_habilidad(self,habilidad):
        if habilidad in self.habilidad:
            self.habilidad.remove(habilidad)
        else:
            return f"habilidad no encontrada!!"
        
    def agregar_objeto(self,objeto):
        if objeto in self.inventario:
            return f"este objeto ya se encuentra!"
        else:
            self.inventario.append(objeto)
            return f"objeto agregado"
        
    def quitar_objeto(self,objeto):
        if objeto in self.inventario:
            return f"objeto no encontrado!!"
        else:
            return self.inventario.remove(objeto)
        
def datos(self):
    print(f"NOMBRE: {self.nombre}")
    print(f"ESPECIE: {self.especie}")
    print(f"PLANETA: {self.planeta}")
    print (f"HABILIDADES:")
    for h in self.habilidad:
        print(f"--> {h.nombre} : {h.nivel_habilidad}")
        









