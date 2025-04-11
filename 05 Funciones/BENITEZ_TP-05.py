from math import pi

# 1. Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.
def imprimir_hola_mundo():
    print("Hola Mundo!")

# 2. Crear una función llamada saludar_usuario(nombre) que reciba
#  como parámetro un nombre y devuelva un saludo personalizado.
#  Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de
# volver: “Hola Marcos!”. Llamar a esta función desde el programa
#  principal solicitando el nombre al usuario.
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

# 3. Crear una función llamada informacion_personal(nombre, apellido,
#  edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#  [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe
# dir los datos al usuario y llamar a esta función con los valores in
# gresados.
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el ra
# dio como parámetro y devuelva el área del círculo. calcular_peri
# metro_circulo(radio) que reciba el radio como parámetro y devuel
# va el perímetro del círculo. Solicitar el radio al usuario y llamar am
# bas funciones para mostrar los resultados.
def calcular_area_circulo(radio):
    return pi * radio ** 2
def calcular_perimetro_circulo(radio):
    return 2 * pi * radio

# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mos
# trar el resultado usando esta función.
def segundos_a_horas(segundos):
    return segundos / 3600

# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la fun
# ción.
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i}: {i * numero}")

# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resulta
# do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re
# sultados de forma clara.
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:
        division = a / b
    else:
        division = "Error: División poro cero"
    return (suma, resta, multiplicacion, division)

# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun
# ción para mostrar el resultado con dos decimales.
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.
def celsius_a_fahrenheit(celsius):
    return (celsius * 1.8) + 32

# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# Programa Principal
imprimir_hola_mundo() # 1

saludar_usuario("Rodrigo") # 2

nombre = input("Por favor, ingrese su nombre: ") # 3
apellido = input("Por favor, ingrese su apellido: ") # 3
edad = input("Por favor, ingrese su edad: ") # 3
residencia = input("Por favor, ingrese su residencia: ") # 3
informacion_personal(nombre, apellido, edad, residencia) # 3

radio = float(input("Por favor, ingrese el radio del círculo: ")) # 4
area = calcular_area_circulo(radio) # 4
print(f"El área del círculo con radio {radio} es {area:.2f}") # 4
perimetro = calcular_perimetro_circulo(radio) # 4
print(f"El perímetro del círculo cn radio {radio} es {perimetro:.2f}") # 4

segundos = int(input("Por favor, ingresa la cantidad de segundos: ")) # 5
horas = segundos_a_horas(segundos) # 5
print(f"{segundos} segundos corresponden a {horas:.2f} {"horas" if horas > 1 else "hora"}") # 5

numero = int(input("Por favor, ingrese un número entero: ")) # 6
tabla_multiplicar(numero) # 6

num_a, num_b = 24, 2 # 7
suma, resta, multiplicacion, division = operaciones_basicas(num_a, num_b) # 7
print(f"""
Resultados para {num_a} y {num_b}:
{num_a} + {num_b} = {suma}
{num_a} - {num_b} = {resta}
{num_a} * {num_b} = {multiplicacion}
{num_a} / {num_b} = {division}
""") # 7

peso = float(input("Por favor, ingrese su peso en kilogramos: ")) # 8
altura = float(input("Por favor, ingrese su altura en metros: ")) # 8
imc = calcular_imc(peso, altura) # 8
print(f"El índice de masa corporal (IMC) para los valores: {peso} kg - {altura} m es: {imc:.2f}") # 8

celsius = float(input("Por favor, ingrese una temperatura en grados Celsius: ")) # 9
fahrenheit = celsius_a_fahrenheit(celsius) # 9
print(f"{celsius} grados celsius, equivalen a {fahrenheit:.2f} grados fahrenheit") # 9

num_1 = float(input("Por favor, ingrese el primer número: ")) # 10
num_2 = float(input("Por favor, ingrese el segundo número: ")) # 10
num_3 = float(input("Por favor, ingrese el tercer número: ")) # 10
promedio = calcular_promedio(num_1, num_2, num_3) # 10
print(f"El promedio de los números: {num_1} - {num_2} - {num_3} es: {promedio:.2f}") # 10