class Personaje:
    def __init__(self,nombre,especie,planeta):
        self.nombre = nombre
        self.especie = especie
        self.planeta = planeta
        self.habilidad = []
        self.inventario = []
        self.nivel_poder = []

    def get_nombre(self):
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
            return f"habilidad eliminada"
        else:
            return f"habilidad no encontrada!!"
        
    def agregar_objeto(self,objeto):
        if objeto in self.inventario:
            return f"este objeto ya se encuentra!"
        else:
            self.inventario.append(objeto)
            # si el objeto tiene atributo nivel_poder, lo guardamos
            if hasattr(objeto, "nivel_poder"):
                self.nivel_poder.append(objeto.nivel_poder)
            return f"objeto agregado"
        
    def quitar_objeto(self,objeto):
        if objeto in self.inventario:
            self.inventario.remove(objeto)
            # intentar remover su nivel de poder asociado si existe
            try:
                if hasattr(objeto, "nivel_poder"):
                    self.nivel_poder.remove(objeto.nivel_poder)
            except ValueError:
                pass
            return f"objeto eliminado"
        else: 
            return f"objeto no encontrado!!"
    
    def datos(self):
        print(f"NOMBRE: {self.nombre}")
        print(f"ESPECIE: {self.especie}")
        print(f"PLANETA: {self.planeta}")
        print (f"HABILIDADES:")
        for h in self.habilidad:
            nombre = getattr(h, "nombre", str(h))
            nivel = getattr(h, "nivel_habilidad", "")
            print(f"-->{nombre} -->nivel:{nivel}")
        print(f"OBJETOS:")
        for o in self.inventario:
            nombre = getattr(o, "nombre", str(o))
            nivel = getattr(o, "nivel_poder", "")
            print(f"--->{nombre}  -->nivel de poder:{nivel}")
        
#   def datos(self):
#     print(f"NOMBRE: {self.nombre}")
#     print(f"ESPECIE: {self.especie}")
#     print(f"PLANETA: {self.planeta}")
#     print (f"HABILIDADES:")
#     for h in self.habilidad:
#         print(f"-->{h.nombre} -->nivel:{h.nivel_habilidad}")
#     print(f"OBJETOS:")
#     for o in self.inventario:
#         print(f"--->{o.nombre}  -->nivel de poder:{o.nivel_poder}")

    # def sumar_poder(nivel_poder):
    #     if len(nivel_poder) == 0:
    #         return 0+
    #     else:
    #         return nivel_poder[0] + sumar_poder(nivel_poder[1: ])
        
    def calcular_poder(self):
        # aca hay recursivad
        def _sumar(lista):
            if not lista:
                return 0
            return lista[0] + _sumar(lista[1:])
        base = _sumar(self.nivel_poder)

        # y aca tenemos para las transformaciones, se multiplica el poder, por la multiplicador de la transformacion
        multiplicador = 1
        for h in self.habilidad:
            m = getattr(h, "multiplicador", None)
            if m is not None:
                multiplicador *= m
            else:
                nombre = getattr(h, "nombre", "").lower()
                if nombre == "transformacion" and hasattr(h, "multiplicador"):
                    multiplicador *= getattr(h, "multiplicador")
        return base * multiplicador








