import heapq

class Mision:
    def __init__(self, nombre):
        self.nombre = nombre
        self.descripcion = ""
        self.recompensa = []
        self.enemigos = []

    def set_nombre_mision(self, nombre):
        self.nombre = nombre

    def set_descirpcion_mision(self, descripcion):
        self.descripcion = descripcion

    def agregar_recompensa_mision(self, recompensa):
        self.recompensa.append(recompensa)
        print(f'Se agregó "{recompensa}" a la lista de recompensas')

    def quitar_recompensa_mision(self, recompensa):
        if recompensa in self.recompensa:
            self.recompensa.remove(recompensa)
            print(f'Se eliminó "{recompensa}" de la lista de recompensas')
        else:
            print(f'"{recompensa}" no se encuentra en la lista de recompensas')

    def agregar_enemigo_mision(self, enemigo):
        self.enemigos.append(enemigo)

    def quitar_enemigo_mision(self, enemigo):
        if enemigo in self.enemigos:
            self.enemigos.remove(enemigo)
            print(f'Se eliminó "{enemigo}" de la lista de enemigos')
        else:
            print(f'"{enemigo}" no se encuentra en la lista de enemigos')

    def calcular_amenaza_mision(self):
        return sum(enemigo.nivel_poder for enemigo in self.enemigos)

    def calcular_recompensa_mision(self):
        return sum(recompensa.nivel_poder for recompensa in self.recompensa)

    def informacion_mision(self):
        print(f"Nombre: {self.nombre}")
        print(f"Descripcion: {self.descripcion}")
        print(f"Recompensa: {self.recompensa}")
        print(f"Enemigos: {self.enemigos}")
        print(f"Amenaza: {self.calcular_amenaza_mision()}")
        print(f"Recompensa total: {self.calcular_recompensa_mision()}")

class Cola_Prioridad_Misiones:
    def __init__(self, criterio="amenaza"):
        self.cola = []
        self.criterio = criterio  # "amenaza" o "recompensa", si no se especifica por default sera "amenaza"

    def prioridad(self, mision):
        if self.criterio == "amenaza":
            return mision.calcular_amenaza_mision()
        elif self.criterio == "recompensa":
            return mision.calcular_recompensa_mision()
        else:
            raise ValueError("Criterio inválido")

    def agregar_mision(self, mision):
        prioridad = self.prioridad(mision)
        heapq.heappush(self.cola, (-prioridad, mision))  
        print(f"Misión '{mision.nombre}' agregada con prioridad: {prioridad}")

    def sacar_mision(self):
        if not self.cola:
            print("No hay misiones en la cola")
            return None
        prioridad, mision = heapq.heappop(self.cola)
        return mision

    def mostrar_misiones(self):
        print("---- Cola de Prioridades (Ordenada) ----")
        copia = self.cola.copy()
        temp = []
        while copia:
            prioridad, mision = heapq.heappop(copia)
            temp.append((-prioridad, mision))
        for prioridad, mis in temp:
            print(f"{mis.nombre} | Prioridad = {prioridad}")




  
  

