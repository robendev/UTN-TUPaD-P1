import random

# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
for i in range(101):
    print(f"Número: {i}")

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
# dígitos que contiene.
numero = int(input("Por favor, ingrese un número entero: "))
cociente = abs(numero)
cant_digitos = 0
while cociente != 0:
    cociente //= 10
    cant_digitos += 1
print(f"El número {numero} contiene {cant_digitos} {'dígito' if cant_digitos == 1 else "dígitos"}")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
# dados por el usuario, excluyendo esos dos valores.
sumatoria = 0
numero_inicial = int(input("Por favor, ingrese un número inicial: "))
numero_final = int(input("Por favor, ingrese un número final: "))
if numero_inicial == numero_final:
    print("Los números ingresados son iguales, no hay números enteros entre ellos para sumar")
else:
    inicio, fin = (numero_inicial, numero_final) if numero_inicial <= numero_final else (numero_final, numero_inicial)
    for i in range(inicio + 1, fin):
        sumatoria += i
    print(f"La sumatoria de los números entre {inicio} y {fin} es: {sumatoria}")

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
# un 0.
total_acumulado = 0
numero = int(input("Por favor, ingrese un número entero (0 Para finalizar): "))
while numero != 0:
    total_acumulado += numero
    numero = int(input("Por favor, ingrese un número entero (0 Para finalizar): "))
print(f"El total acumulado de los números ingresados es: {total_acumulado}")

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
intentos = 0
numero_aleatorio = random.randint(0, 1)
numero = int(input("Intenta adivinar el número, ingresa un número entre 0 y 9: "))
while numero != numero_aleatorio:
    intentos += 1
    numero = int(input("Intenta adivinar el número, ingresa un número entre 0 y 9: "))
intentos += 1
print(f"Has acertado, necesitaste {intentos} {'intentos' if intentos > 1 else 'intento'} ")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
# entre 0 y 100, en orden decreciente.
for i in range(98, 0, -2):
    print(f"Número: {i}")

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
# número entero positivo indicado por el usuario.
sumatoria = 0
numero = int(input("Por favor, ingrese un número entero positivo: "))
for i in range(0, numero):
    sumatoria += i
print(f"La sumatoria entre {0} y {numero} es: {sumatoria}")

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).
CANT_NUMEROS = 100
cant_pares = 0
cant_impares = 0
cant_positivos = 0
cant_negativos = 0
for i in range(CANT_NUMEROS):
    numero = int(input(f"Número {i + 1}: "))
    if numero % 2 == 0:
        cant_pares += 1
    else:
        cant_impares += 1
    
    if numero > 0:
        cant_positivos += 1
    elif numero < 0:
        cant_negativos += 1
print(f"""
Cantidad de números pares: {cant_pares}
Cantidad de números impares: {cant_impares}
Cantidad de números positivos: {cant_positivos}
Cantidad de números negativos: {cant_negativos}
""")

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
# poder procesar 100 números cambiando solo un valor).
CANT_NUMEROS = 5
sumatoria = 0
for i in range(CANT_NUMEROS):
    numero = int(input(f"Número {i + 1}: "))
    sumatoria += numero
print(f"La media de los valores ingresados es: {sumatoria / CANT_NUMEROS}")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
numero = int(input("Por favor, ingrese un número: "))
cociente = abs(numero)
texto = ''
while cociente != 0:
    resto = cociente % 10
    texto += str(resto)
    cociente //= 10
if numero < 0:
    texto = "-" + texto
print(f"El número {numero} invertido es: {texto if numero != 0 else 0}")