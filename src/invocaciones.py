from nodo_bi import *
from nodo_ge import *
from personaje import *
from habilidad import *
from objeto import *
from arbol_binario import *
from arbol_general import *

def linea_separadora(simbolo="~",largo=90):
    print(f"{simbolo}" * largo)



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
linea_separadora()
personaje2.datos()
linea_separadora()
personaje3.datos()
linea_separadora()
print(f"{personaje1.nombre} tiene una suma total de poder de: {personaje1.calcular_poder()}")
print(f"{personaje2.nombre} tiene una suma total de poder de: {personaje2.calcular_poder()}")
print(f"{personaje3.nombre} tiene una suma total de poder de: {personaje3.calcular_poder()}")

#llamadas al arbol binario
arbol_binario = ArbolBinario()
arbol_binario.agregar(personaje1)
arbol_binario.agregar(personaje2)
arbol_binario.agregar(personaje3)
print("Recorrido Inorden:")
print(arbol_binario.inorden())
linea_separadora()
print("Recorrido Preorden:")
print(arbol_binario.preorden())
linea_separadora()
print("Recorrido Postorden:")
print(arbol_binario.postorden())


#busqueda de personaje por poder
poder_a_buscar = 275
personaje_encontrado = arbol_binario.busqueda(poder_a_buscar)
linea_separadora()
if personaje_encontrado:
    print(f"Personaje encontrado con poder {poder_a_buscar}: {personaje_encontrado.nombre}")
else:
    print(f"No se encontró ningún personaje con poder {poder_a_buscar}.")

#llamadas del arbol general
arbol_general = arbol_general(geNodo(personaje1))
nodo_hab1 = geNodo(habilidad1)
nodo_hab2 = geNodo(habilidad2)
nodo_hab3 = geNodo(habilidad3)
nodo_tra1 = geNodo(transformacion1)

arbol_general.agregar_hijo(arbol_general.raiz, nodo_hab1)
arbol_general.agregar_hijo(nodo_hab1, nodo_hab2)
arbol_general.agregar_hijo(nodo_hab2, nodo_hab3)

arbol_general.agregar_hijo(arbol_general.raiz, nodo_tra1)
# metodo de arbol General
print("Recorrido Inorden del Arbol General:")
print(arbol_general.inorden())
linea_separadora()
print("Recorrido Preorden del Arbol General:")
print(arbol_general.preorden())
linea_separadora()
print("Recorrido Postorden del Arbol General:")
print(arbol_general.postorden())

# busqueda en arbol general
nombre_a_buscar = "Repostero"
nodo_encontrado = arbol_general.busqueda(nombre_a_buscar)
linea_separadora()
if nodo_encontrado:
    print(f"Nodo encontrado con nombre '{nombre_a_buscar}': {nodo_encontrado.datos.nombre}")
else:
    print(f"No se encontró ningún nodo con nombre '{nombre_a_buscar}'.")
