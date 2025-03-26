# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola Mundo!")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando 
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir 
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para 
# realizar la impresión por pantalla.
nombre = input("Por favor, ingrese su nombre: ")
print(f"Hola {nombre}!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e 
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa 
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar 
# la impresión por pantalla.
nombre = input("Por favor, ingrese su nombre: ")
apellido = input("Por favor, ingrese su apellido: ")
edad = input("Por favor, ingrese su edad: ")
lugar_de_residencia = input("Por favor, ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_de_residencia}")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y 
# su perímetro.
radio_circulo = int(input("Por favor, ingrese el radio del círculo: "))
print(f"El área es: {3.1416 * radio_circulo ** 2} - El perímetro es: {2 * 3.1416 * radio_circulo}")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a 
# cuántas horas equivale.
cantidad_de_segundos = int(input("Por favor, ingrese una cantidad de segundos: "))
print(f"{cantidad_de_segundos} segundos equivalen a {cantidad_de_segundos / 3600} horas")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de 
# multiplicar de dicho número.
numero = int(input("Por favor, ingrese un número: "))

print(f"""
{numero} x 1 = {numero * 1}
{numero} x 2 = {numero * 2}
{numero} x 3 = {numero * 3}
{numero} x 4 = {numero * 4}
{numero} x 5 = {numero * 5}
{numero} x 6 = {numero * 6}
{numero} x 7 = {numero * 7}
{numero} x 8 = {numero * 8}
{numero} x 9 = {numero * 9}
{numero} x 10 = {numero * 10}
""")

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por 
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
numero1 = int(input("Por favor, ingrese un número entero distinto de 0: "))
numero2 = int(input("Por favor, ingrese un número entero distinto de 0: "))
print(f"{numero1} + {numero2}: {numero1 + numero2}")
print(f"{numero1} - {numero2}: {numero1 - numero2}")
print(f"{numero1} * {numero2}: {numero1 * numero2}")
print(f"{numero1} / {numero2}: {numero1 / numero2}")

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice 
# de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente 
# modo: IMC = peso en kg / altura en m ** 2
altura = float(input("Por favor, ingrese su altura: "))
peso = float(input("Por favor, ingrese su peso: "))
print(f"Índice de masa corporal: {peso / (altura ** 2)}")

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por 
# pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia: 
# T𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9/5. 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32
temperatura_grados_celsius = float(input("Por favor, ingrese una temperatura en grados Celsius: "))
print(f"El equivalente de {temperatura_grados_celsius} grados Celsius, a Fahrenheit es de: {temperatura_grados_celsius * 1.8 + 32} grados")

# 10) Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de 
# dichos números.
numero1 = float(input("Por favor, ingrese un número: "))
numero2 = float(input("Por favor, ingrese un número: "))
numero3 = float(input("Por favor, ingrese un número: "))
print(f"El promedio de los números {numero1}, {numero2}, y {numero3} es de: {(numero1 + numero2 + numero3) / 3}")