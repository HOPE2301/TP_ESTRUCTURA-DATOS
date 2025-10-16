# importe todas las clases necesarias para la invoaciones, y cree instancias para probar el codigo.
from personaje import Personaje
from habilidad import Habilidad
from objeto import Objeto
from funciones_comunes import linea_separadora


personaje1 = Personaje ("Estif", "Humano", "Tierra")
personaje2 = Personaje ("Lucas", "Patoide", "Marte")
personaje3 = Personaje ("Camila", "Insectoide", "Marte")

personaje1.info()
linea_separadora()
personaje2.info()
linea_separadora()
personaje3.info()

habilidad1 = Habilidad ("cocinar", 1, 5)
habilidad2 = Habilidad ("pelear", 3, 15)
objeto1 = Objeto ("espada", 10)
personaje1.agregar(habilidad1)
personaje1.agregar(habilidad2)
personaje1.agregar(objeto1)

linea_separadora()

personaje1.info()