class Personaje:
      def __init__(self,nombre,especie,planeta,nivel_poder=0):
            self.nombre = nombre
            self.especie = especie
            self.planeta = planeta
            self.habilidad = []
            self.inventario = []
            self.nivel_poder = nivel_poder

      def get_nombre (self):
            return self.nombre

      def set_nombre(self,nombre):
            self.nombre = nombre 

      def get_especie (self):
            return self.especie

      def set_especie(self,especie):
            self.especie = especie         

      def get_planeta(self):
            return self.planeta

      def set_planeta(self,planeta):
            self.planeta = planeta

      #Funcion que muestra la informacion de del personaje.
      def info(self):
            print  (f" el personaje: {self.nombre} es de la especie {self.especie} y pertenece al planeta {self.planeta}")
            if self.habilidad:
                  print("Habilidades:")
                  for hab in self.habilidad:
                        hab.datos()
            if self.inventario:
                  print("Inventario:")
                  for obj in self.inventario:
                        obj.datos()
#Explicaion de esta funcion, esta funcion recibe un dato, y verifica si es una habilidad o un objeto, y lo agrega a la lista correspondiente, hasattr() es una funcion que ve si el objeto tiene un metodo que pasa por atributo, y callable() ve si es un metodo que se puede llamar.
      def agregar(self, dato):
            if hasattr(dato, "soy_habilidad") and callable(getattr(dato, "soy_habilidad")):
                  self.habilidad.append(dato)
            elif hasattr(dato, "soy_objeto") and callable(getattr(dato, "soy_objeto")):
                  self.inventario.append(dato)
            else:
                  raise TypeError("dato debe exponer get_poder (habilidad) o get_utilidad (objeto)")









