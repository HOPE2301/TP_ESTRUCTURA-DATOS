class arbol_general:
    def __init__(self, raiz):
        self.raiz = raiz

    def _nombre_de(self, datos):
        if hasattr(datos, "nombre"):
            nombre = getattr(datos, "nombre")
            if callable(nombre):
                try:
                    return nombre()
                except Exception:
                    return str(nombre)
            return nombre
        return str(datos)

    def agregar_hijo(self, nodo_padre, nodo_hijo):
        nodo_padre.agregar_hijo(nodo_hijo)

    def inorden(self, nodo=None, padre_nombre=None):
        if nodo is None:
            nodo = self.raiz
        listado = []
        for hijo in nodo.hijos:
            listado += self.inorden(hijo, padre_nombre=self._nombre_de(nodo.datos) if padre_nombre is None else padre_nombre)
        nombre_actual = self._nombre_de(nodo.datos)
        if padre_nombre is not None:
            listado.append(f"{padre_nombre} -> {nombre_actual}")
        else:
            listado.append(f"Personaje: {nombre_actual}")
        return listado

    def preorden(self, nodo=None, padre_nombre=None):
        if nodo is None:
            nodo = self.raiz
        listado = []
        nombre_actual = self._nombre_de(nodo.datos)
        if padre_nombre is not None:
            listado.append(f"{padre_nombre} -> {nombre_actual}")
        else:
            listado.append(f"Personaje: {nombre_actual}")
        for hijo in nodo.hijos:
            listado += self.preorden(hijo, padre_nombre=nombre_actual if padre_nombre is None else padre_nombre)
        return listado

    def postorden(self, nodo=None, padre_nombre=None):
        if nodo is None:
            nodo = self.raiz
        listado = []
        for hijo in nodo.hijos:
            listado += self.postorden(hijo, padre_nombre=self._nombre_de(nodo.datos) if padre_nombre is None else padre_nombre)
        nombre_actual = self._nombre_de(nodo.datos)
        if padre_nombre is not None:
            listado.append(f"{padre_nombre} -> {nombre_actual}")
        else:
            listado.append(f"Personaje: {nombre_actual}")
        return listado

    def busqueda(self, nombre_buscar, nodo=None):
        if nodo is None:
            nodo = self.raiz
        nombre_buscar_lower = nombre_buscar.lower()
        if nombre_buscar_lower == self._nombre_de(nodo.datos).lower():
            return nodo
        for hijo in nodo.hijos:
            resultado = self.busqueda(nombre_buscar, hijo) 
            if resultado is not None:
                return resultado
        return None
