import math
from collections import deque

# 1) Dado el diccionario precios_frutas 
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 
# 1450} 
# Añadir las siguientes frutas con sus respectivos precios: 
# ● Naranja = 1200 
# ● Manzana = 1500 
# ● Pera = 2300
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
# for fruta, precio in precios_frutas.items():
#     print(f"Key: {fruta} - Value: {precio}")

print("- - - - - - - - - - - - - - - - - - - - - - - - - -")

# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: 
# ● Banana = 1330 
# ● Manzana = 1700 
# ● Melón = 2800
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
# for fruta, precio in precios_frutas.items():
#     print(f"Key: {fruta} - Value: {precio}")

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los 
# precios.
lista_frutas = list(precios_frutas.keys())
# for frutas in lista_frutas:
#     print(f"Fruta: {frutas}")

print("- - - - - - - - - - - - - - - - - - - - - - - - - -")

# 4) Crear una clase llamada Persona que contenga un método __init__ con los atributos 
# nombre, pais y edad y el método saludar. El método saludar debe imprimir por pantalla un 
# mensaje de salud que siga la estructura "¡Hola! Soy [nombre], vivo en [pais] y tengo [edad] 
# años."
class Persona:
    def __init__(self, nombre, pais, edad):
        self._nombre = nombre.title()
        self._pais = pais.title()
        self._edad = edad
    def saludar(self):
        print(f"¡Hola! Soy {self._nombre}, vivo en {self._pais} y tengo {self._edad} años.")
# persona = Persona("Rodrigo", "Argentina", 29)
# persona.saludar()

print("- - - - - - - - - - - - - - - - - - - - - - - - - -")

# 5) Crear una clase llamada Circulo que contenga el atributo radio y los métodos calcular_area y 
# calcular_perimetro. Dichos métodos deben calcular el parámetro correspondiente. 
# Ayuda: el módulo math puede ser de utilidad para usar la constante 𝜋.
class Circulo:
    def __init__(self, radio):
        self._radio = radio
    def calcular_area(self):
        return math.pi * self._radio ** 2
    def calcular_perimetro(self):
        return 2 * math.pi * self._radio
# circulo = Circulo(25.5)
# area = circulo.calcular_area()
# perimetro = circulo.calcular_perimetro()
# print(f"Área del círculo: {area:.2f} - Perimétro del círculo: {perimetro:.2f}")

print("- - - - - - - - - - - - - - - - - - - - - - - - - -")

# 6) Dado un string con paréntesis "()", "{}", "[]", verifica si están correctamente 
# balanceados usando una pila.

def balanceado(item):
    pila = []
    parejas = {")": "(", "}": "{", "]": "["}
    for char in item:
        if char in "({[":
            pila.append(char)
        elif char in ")}]":
            if pila and pila[-1] == parejas[char]:
                pila.pop()
            else:
                return False
    return len(pila) == 0
# print(f"Esta balanceado?: {balanceado("({[]})")}")
# print(f"Esta balanceado?: {balanceado("({[})")}")

print("- - - - - - - - - - - - - - - - - - - - - - - - - -")

# 7) Usa una cola para simular un sistema de turnos en un banco. La cola debe permitir: 
# ● Agregar clientes (encolar). 
# ● Atender clientes (desencolar). 
# ● Mostrar el siguiente cliente en la fila.
class Cola:
    def __init__(self):
        self.elementos = deque()
    def encolar(self, elemento):
        self.elementos.append(elemento)
    def desencolar(self):
        return self.elementos.popleft() if not self.esta_vacia() else "La cola está vacía"
    def siguiente_cliente(self):
        siguiente_cliente = self.elementos[0] if not self.esta_vacia() else "La cola está vacía"
        print(f"Siguiente cliente: {siguiente_cliente}")
    def esta_vacia(self):
        return len(self.elementos) == 0
    def get_elementos(self):
        return list(self.elementos)
# cola = Cola()
# cola.encolar("Cliente 1")
# cola.encolar("Cliente 2")
# cola.siguiente_cliente()
# print(cola.desencolar())
# print(cola.get_elementos())
# print(cola.desencolar())
# print(cola.desencolar())
# print(cola.get_elementos())
# cola.siguiente_cliente()

print("- - - - - - - - - - - - - - - - - - - - - - - - - -")

# 8) Crea una lista enlazada que permita insertar nodos al inicio y recorrer la lista para mostrar 
# los valores almacenados.
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo
    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=' ➡️ ')
            actual = actual.siguiente
        print("None")
# lista = ListaEnlazada()
# lista.insertar(3)
# lista.insertar(2)
# lista.insertar(1)
# lista.mostrar()

print("- - - - - - - - - - - - - - - - - - - - - - - - - -")

# 9) Dada una lista enlazada, implementa una función para invertirla. 
# Ejemplo de entrada y salida:
# Lista original: 1 -> 2 -> 3 -> None
# Lista invertida: 3 -> 2 -> 1 -> None
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo
    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=' ➡️ ')
            actual = actual.siguiente
        print("None")
    def invertir(self):
        anterior = None
        actual = self.cabeza # (que es Nodo(1))
        while actual:
            siguiente = actual.siguiente # (que es Nodo(2))
            actual.siguiente = anterior # (Nodo(1).siguiente ahora es None)
            anterior = actual # (anterior ahora es Nodo(1))
            actual = siguiente # (actual ahora es Nodo(2))
        self.cabeza = anterior
# lista = ListaEnlazada()
# lista.insertar(3)
# lista.insertar(2)
# lista.insertar(1)
# print("Lista original:")
# lista.mostrar()
# lista.invertir()
# print("Lista invertida:")
# lista.mostrar()