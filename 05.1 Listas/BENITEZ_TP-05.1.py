from random import randint

# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función 
# range.
lista_multiplos_de_4 = list(range(4, 101, 4))

# 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el 
# penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el 
# indexing con números negativos!
lista_5_elementos = [randint(1, 100) for _ in range(5)]
print(lista_5_elementos)
print(f"Penúltimo elemento: {lista_5_elementos[-2]}")

# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por 
# pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por 
# ejemplo: 
lista_vacia = []
lista_vacia.append("Rodrigo")
lista_vacia.append("Iván")
lista_vacia.append("Benitez")
print(*lista_vacia, end=".\n")

# 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, 
# respectivamente.  Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra 
# en los videos o bien investigar cómo funciona el indexing con números negativos! 
animales = ["perro", "gato", "conejo", "pez"]
animales[1], animales[-1] = "loro", "oso"
print(*animales, sep=", ", end=".\n") # El asterisco (*) se utiliza para desempaquetar (unpack) una lista o cualquier otro iterable.

# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
# El la primera linea se esta inicializando un lista de 5 elementos numericos, luego en la segunda linea se remueve el elemento más
# alto de la lista, al final, en la tercera linea se imprimer la lista resultante...

# 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por 
# pantalla los dos primeros.
lista_numeros_10_al_30 = list(range(10, 31, 5))
print(lista_numeros_10_al_30[0:2])

# 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores 
# cualesquiera.
autos = ["sedan", "polo", "suran", "gol"]

# autos[1:3] = ["polo_actualizado", "suran_actualizado"]

numero_elementos = len(autos)
autos[(numero_elementos // 2) - 1], autos[numero_elementos // 2] = "polo_actualizado", "suran_actualizado"
print(*autos, sep=", ", end=".\n")

# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append 
# directamente. Imprimir la lista resultante por pantalla.
valor_inicial = 5
dobles = []
for _ in range(3):
    valor_doble = valor_inicial * 2
    dobles.append(valor_doble)

    valor_inicial += 5
print(*dobles, sep=", ", end=".\n")

# 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por 
# diferentes clientes: 
# a) Agregar "jugo" a la lista del tercer cliente usando append. 
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente. 
# c) Eliminar "pan" de la lista del primer cliente.  
# d) Imprimir la lista resultante por pantalla

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo") # a
for i in range(len(compras[1])): # b
    if compras[1][i] == "fideos":
        compras[1][i] = "tallarines"
print(compras[1])
compras[0].remove("pan") # c
print(compras[0])
for i, cliente in enumerate(compras, start=1): # d
    print(f"Cliente:", end=" ")
    print(*cliente, sep=", ", end=".\n")

# 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos: 
# ● Posición lista_anidada[0]: 15 
# ● Posición lista_anidada[1]: True 
# ● Posición lista_anidada[2][0]: 25.5 
# ● Posición lista_anidada[2][1]: 57.9 
# ● Posición lista_anidada[2][2]: 30.6 
# ● Posición lista_anidada[3]: False 
# Imprimir la lista resultante por pantalla.
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
for i, elemento in enumerate(lista_anidada):
    if isinstance(elemento, list):
        print(f"lista_anidada[{i}]:", end=" ")
        print(*elemento, sep=", ", end=".\n")
    else:
        print(f"lista_anidada[{i}]:", {elemento}, end=".\n")