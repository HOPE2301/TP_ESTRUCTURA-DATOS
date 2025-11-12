Class Mision:
def __init__(self, nombre):
  self.nombre = nombre
  self.descripcion = ""
  self.recompensa = []
  self.enemigos = []
def set_nombre_mision(self, nombre):
  self.nombre = nombre
def set_descirpcion_mision(self, descripcion):
  self.descripcion = descripcion
def set_recompensa_mision(self, recompensa):
  self.recompensa = recompensa
def agregar_recompensa_mision(self, recompensa):
  self.recompensa.append(recompensa)
  print(f"Se agrego "{recompensa}" a la lista de recompensas")
def quitar_recompensa_mision(self, recompensa):
  if recompensa in self.recompensa:
    self.recompensa.remove(recompensa)
    print(f"Se elimino "{recompensa}" de la lista de recompensas")
  else:
    print(f"{recompensa} no se encuentra en la lista de recompensas")
def set_enemigos_mision(self, enemigos):
  self.enemigos = enemigos
def agregar_enemigo_mision(self, enemigo):
  self.enemigos.append(enemigo)
def quitar_enemigo_mision(self, enemigo):
  if enemigo in self.enemigos:
    self.enemigos.remove(enemigo)
    print(f"Se elimino "{enemigo}" de la lista de enemigos")
  else:
    print(f"{enemigo} no se encuentra en la lista de enemigos")
def calcular_amenaza_mision(self):
  total = sum(enemigo.nivel_poder for enemigo in self.enemigos)
  return total
def calcular_recompensa_mision(self):
  total = sum(recompensa.nivel_poder for recompensa in self.recompensa)
  return total
def informacion_mision(self):
  print(f"Nombre: {self.nombre}")
  print(f"Descripcion: {self.descripcion}")
  print(f"Recompensa: {self.recompensa}")
  print(f"Enemigos: {self.enemigos}")
  print(f"Amenaza: {self.calcular_amenaza_mision()}")
  print(f"Recompensa: {self.calcular_recompensa_mision()}")
  
  

