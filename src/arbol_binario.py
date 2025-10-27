from nodo_bi import *

class ArbolBinario:
    def __init__(self, raiz=None):
        self.raiz = raiz

    def _formato(self, item):
        nombre = None
        if hasattr(item, "nombre"):
            nombre = getattr(item, "nombre")
        else:
            getter = getattr(item, "get_nombre", None)
            if callable(getter):
                nombre = getter()
        poder = None
        if hasattr(item, "calcular_poder") and callable(item.calcular_poder):
            try:
                poder = item.calcular_poder()
            except Exception:
                poder = None
        else:
            if hasattr(item, "nivel_poder"):
                np = getattr(item, "nivel_poder")
                if isinstance(np, (list, tuple)):
                    try:
                        poder = sum(np)
                    except Exception:
                        poder = None
                else:
                    poder = np
        if nombre is None:
            return str(item)
        if poder is None:
            return f"{nombre}"
        return f"{nombre} - Poder: {poder}"

    def agregar(self, data):
        if self.raiz is None:
            self.raiz = BiNodo(data)
        else:
            self.raiz.agregar(data)

    def inorden(self):
        listado = []
        if self.raiz is not None:
            if self.raiz.izquierdo:
                listado += ArbolBinario(self.raiz.izquierdo).inorden()
            listado.append(self._formato(self.raiz.data))
            if self.raiz.derecho:
                listado += ArbolBinario(self.raiz.derecho).inorden()
        return listado

    def preorden(self):
        listado = []
        if self.raiz is not None:
            listado.append(self._formato(self.raiz.data))
            if self.raiz.izquierdo:
                listado += ArbolBinario(self.raiz.izquierdo).preorden()
            if self.raiz.derecho:
                listado += ArbolBinario(self.raiz.derecho).preorden()
        return listado

    def postorden(self):
        listado = []
        if self.raiz is not None:
            if self.raiz.izquierdo:
                listado += ArbolBinario(self.raiz.izquierdo).postorden()
            if self.raiz.derecho:
                listado += ArbolBinario(self.raiz.derecho).postorden()
            listado.append(self._formato(self.raiz.data))
        return listado