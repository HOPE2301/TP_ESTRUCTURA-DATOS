#Modifique la clase habilidad para que tenga el atributo de nivel_poder
class Habilidad():
      def __init__(self, nombre,nivel,nivel_poder=0):
            self.nombre = nombre
            self.nivel = nivel 
            self.nivel_poder = nivel_poder

      def datos(self):
            print (f"   la habilidad {self.nombre} es de nivel: {self.nivel} y tiene un poder de {self.nivel_poder}")
      #Esta funciona sirver para el metodo agregar de la clase personaje, es un tipo de duck typing
      def soy_habilidad(self):
            return True
