from personaje import *
from habilidad import *
from objeto import *


#invocaciones:
personaje1 = Personaje("Estif", "Humano", "Tierra")
personaje2 = Personaje("Lucas", "Patoide", "Marte")
personaje3 = Personaje("Camila", "Insectoide", "Marte")

habilidad1 = Habilidad("Cocinero", "Principiante")
habilidad2 = Habilidad("Repostero","intermedio" )
habilidad3 = Habilidad("Combate", "Intermedio")
habilidad4 = Habilidad("Velocidad", "Experto")
habilidad5 = Habilidad("Cazar", "Principiante")
habilidad6 = Habilidad("Volar", "Intermedio")

personaje1.agregar_habilidad(habilidad1)
personaje1.agregar_habilidad(habilidad2)
personaje2.agregar_habilidad(habilidad3)
personaje3.agregar_habilidad(habilidad4)
personaje3.agregar_habilidad(habilidad5)
personaje3.agregar_habilidad(habilidad6)

objeto1 = Objeto("Espada", 20)
objeto2 = Objeto("Sarten", 50)
objeto3 = Objeto("Arco", 100)
objeto4 = Objeto("Capa",65)
objeto5 = Objeto("Martillo",95)
objeto6 = Objeto("Chuchillo",130)

personaje1.agregar_objeto(objeto2)
personaje2.agregar_objeto(objeto1)
personaje3.agregar_objeto(objeto3)
personaje2.agregar_objeto(objeto4)
personaje1.agregar_objeto(objeto6)
personaje1.agregar_objeto(objeto5)

personaje1.quitar_habilidad(habilidad2)
personaje2.quitar_objeto(objeto4)
personaje3.quitar_habilidad(habilidad4)

datos(personaje1)
print(f"---------------------------------------")
datos(personaje2)
print(f"---------------------------------------")
datos(personaje3)
print(f"---------------------------------------")
print(f"{personaje1.nombre} tiene una suma total de poder de:",sumar_poder(personaje1.nivel_poder))
print(f"{personaje2.nombre} tiene una suma total de poder de:",sumar_poder(personaje2.nivel_poder))
print(f"{personaje3.nombre} tiene una suma total de poder de:",sumar_poder(personaje3.nivel_poder))



