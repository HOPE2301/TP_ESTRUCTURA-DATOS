class Objeto():
       def __init__(self, nombre,nivel_poder):
              self.nombre = nombre
              self.nivel_poder = nivel_poder

       def datos(self):
              print (f"     el objeto {self.nombre} tiene un nivel de poder de {self.nivel_poder} ")
       #Esta funciona sirver para el metodo agregar de la clase personaje, es un tipo de duck typing
       def soy_objeto(self):
              return True