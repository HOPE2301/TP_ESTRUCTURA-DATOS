from nodo_bi import *
from nodo_ge import *
from personaje import *
from habilidad import *
from objeto import *
from arbol_binario import *
from arbol_general import *


#invocaciones:
personaje1 = Personaje("Estif", "Humano", "Tierra")
personaje2 = Personaje("Lucas", "Patoide", "Marte")
personaje3 = Personaje("Camila", "Insectoide", "Marte")

habilidad1 = Habilidad("Cocinero", "Principiante")
habilidad2 = Habilidad("Repostero","intermedio" )
habilidad3 = Habilidad("Chef", "Experto")
habilidad4 = Habilidad("Velocidad", "Experto")
habilidad5 = Habilidad("Cazar", "Principiante")
habilidad6 = Habilidad("Volar", "Intermedio")

transformacion1 = transformacion("Profesional", 2)

personaje1.agregar_habilidad(habilidad1)
personaje1.agregar_habilidad(habilidad2)
personaje2.agregar_habilidad(habilidad3)
personaje3.agregar_habilidad(habilidad4)
personaje3.agregar_habilidad(habilidad5)
personaje3.agregar_habilidad(habilidad6)

personaje2.agregar_habilidad(transformacion1)

objeto1 = Objeto("Espada", 20)
objeto2 = Objeto("Sarten", 50)
objeto3 = Objeto("Arco", 100)
objeto4 = Objeto("Capa",65)
objeto5 = Objeto("Martillo",95)
objeto6 = Objeto("Chuchillo",130)

personaje1.agregar_objeto(objeto2)
personaje1.agregar_objeto(objeto6)
personaje1.agregar_objeto(objeto5)
personaje2.agregar_objeto(objeto1)
personaje3.agregar_objeto(objeto3)
personaje2.agregar_objeto(objeto4)

personaje1.quitar_habilidad(habilidad2)
personaje2.quitar_objeto(objeto4)
personaje3.quitar_habilidad(habilidad4)

personaje1.datos()
print(f"---------------------------------------")
personaje2.datos()
print(f"---------------------------------------")
personaje3.datos()
print(f"---------------------------------------")
print(f"{personaje1.nombre} tiene una suma total de poder de: {personaje1.calcular_poder()}")
print(f"{personaje2.nombre} tiene una suma total de poder de: {personaje2.calcular_poder()}")
print(f"{personaje3.nombre} tiene una suma total de poder de: {personaje3.calcular_poder()}")