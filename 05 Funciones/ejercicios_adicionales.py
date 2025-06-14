# 1. Crea una función tabla_multiplicar que reciba un número entero positivo. 
# 2. Devuelve una lista con su tabla de multiplicar del 1 al 10. 
# o Ejemplo: Para 3 → [3, 6, 9, ..., 30].
def tabla_multiplicar(n, n_range):
    if not isinstance(n, int) or not isinstance(n_range, int):
        raise ValueError("Ambos parámeros deben ser enteros.")
    if n < 0 or n_range < 1:
        raise ValueError("El número debe ser positivo y el rango mayor que cero.")
    return [n * i for i in range(1, n_range + 1)] # [nueva_expresión for elemento in iterable] (list comprehensions)
try:
    result = tabla_multiplicar(3, 10)
    print(f"Tabla: {result}")
except ValueError as e:
    print(f"Error: {e}")

# 1. Define una función suma_pares que reciba una lista de enteros. 
# 2. Retorna la suma de los números pares. 
# o Ejemplo: Para [1, 2, 3, 4, 5, 6] → 12.
def suma_pares(n_enteros):
    return sum(n for n in n_enteros if isinstance(n, int) and n % 2 == 0)
print(suma_pares([3, 1, 4, 2.0, 2, 7, 8, "10", 6.0])) # 14

# 1. Crea una función rectángulo que reciba longitud y anchura. 
# 2. Retorna una tupla con el área y el perímetro. 
# o Fórmulas: 
# ▪ Área = longitud * anchura. 
# ▪ Perímetro = 2 * (longitud + anchura).
def rectangulo(longitud, anchura):
    if not(isinstance(longitud, (int, float)) and isinstance(anchura, (int, float))):
        raise TypeError("Ambos valores deben ser números (int o float).")
    if longitud <= 0 or anchura <= 0:
        raise ValueError("La longitud y la anchura deben ser mayores que cero.")
    area, perimetro = longitud * anchura, 2 * (longitud + anchura)
    return (area, perimetro)
print(rectangulo(5, 3)) # Resultado: (15, 16)

# 1. Define una función convertir_temperatura que reciba: 
# o Temperatura en Celsius. 
# o Unidad de destino ("F" o "K"). 
# 2. Retorna la temperatura convertida usando: 
# o Fahrenheit: F = C * 9/5 + 32. 
# o Kelvin: K = C + 273.15.
def convertir_temperatura(temperatura_celsius, unidad_destino):
    if unidad_destino not in ("F", "K"):
        raise ValueError("Unidad no válida.")
    return temperatura_celsius * 1.8 + 32 if unidad_destino == "F" else temperatura_celsius + 273.15
try:
    print(convertir_temperatura(25, "X"))
except ValueError as e:
    print(f"Error: {e}")

# 1. Crea una función es_primo que reciba un entero positivo. 
# 2. Retorna True si es primo (solo divisible por 1 y sí mismo), False en caso 
# contrario. 
# o Ejemplo: 7 → True, 8 → False.
def es_primo(n):
    if n <= 1:
        return  False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print(es_primo(7))

# 1. Define una función promedio_calificaciones que reciba una lista de notas 
# (0 a 10). 
# 2. Retorna el promedio. Si la lista está vacía, retorna 0. 
# o Ejemplo: [8.5, 9.0, 7.5, 8.0] → 8.25.
def promedio_calificaciones(n_notas):
    if len(n_notas) == 0:
        return 0
    return sum(n_notas) / len(n_notas) # sum() acepta directamente una lista, no hace falta recorrer los elementos sum(n for n in n_notas)
print(promedio_calificaciones([6, 7.6, 8.2, 3.2, 10]))

# 1. Usa dos funciones: 
# o validar_entrada: Verifica si un número es entero no negativo. 
# o factorial: Calcula el factorial (ej: 5! = 120). 
# 2. El programa principal debe: 
# o Pedir un número al usuario. 
# o Validarlo y mostrar el factorial o un error.
def validar_entrada(n):
    if not isinstance(n, int):
        raise TypeError("El valor debe ser un número entero.")
    if n < 0:
        raise ValueError("El número debe ser no negativo.")
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
try:
    numero = int(input("Ingrese un número entero no negativo: "))
    validar_entrada(numero)
    print(f"El factorial de {numero} es {factorial(numero)}")
except (TypeError, ValueError) as e:
    print("Error:", e)

# 1. Usa dos funciones: 
# o es_divisible: Retorna True si un número divide a otro. 
# o es_primo: Usa es_divisible para verificar si es primo. 
# 2. El programa principal pide un número y muestra si es primo. 
def es_divisible(n, divisor):
    return n % divisor == 0
def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if es_divisible(n, i):
            return False
    return True
numero = int(input("Ingrese un número: "))
if es_primo(numero):
    print(f"{numero} es primo.")
else:
    print(f"{numero} no es primo.")

# 1. Usa tres funciones: 
# o convertir_a_fahrenheit: Convierte Celsius a Fahrenheit. 
# o convertir_a_kelvin: Convierte Celsius a Kelvin. 
# o menu_conversion: Muestra un menú para elegir la unidad. 
# 2. El programa principal: 
# o Pide la temperatura en Celsius. 
# o Muestra el resultado según la unidad elegida.
def convertir_a_fahrenheit(c):
    return c * 1.8 + 32
def convertir_a_kelvin(c):
    return c + 273.15
def menu_conversion():
    print("Seleccione la unidad de destino:")
    print("1. Fahrenheit")
    print("2. Kelvin")
    opcion = input("Ingrese 1 o 2: ")
    if opcion == "1":
        return "F"
    elif opcion == "2":
        return "K"
    else:
        print("Opción no válida. Se usará Fahrenheit por defecto.")
        return "F"
celsius = float(input("Ingrese la temperatura en Celsius: "))
unidad = menu_conversion()
if unidad == "F":
    print(f"{celsius}°C = {convertir_a_fahrenheit(celsius):.2f}°F")
else:
    print(f"{celsius}°C = {convertir_a_kelvin(celsius):.2f}K")

# 1. Usa tres funciones: 
# o validar_dimensiones: Verifica que longitud y anchura sean positivas. 
# o calcular_area: Retorna el área del rectángulo. 
# o calcular_perimetro: Retorna el perímetro. 
# 2. El programa principal: 
# o Pide las dimensiones al usuario. 
# o Valida y muestra resultados o un error.
def validar_dimensiones(longitud, anchura):
    if not(isinstance(longitud, (int, float)) and isinstance(anchura, (int, float))):
        raise TypeError("Las dimensiones deben ser números decimales (float).")
    if longitud <= 0 or anchura <= 0:
        raise ValueError("Las dimensiones deben ser mayores que cero.")
    return True
def calcular_area(longitud, anchura):
    return longitud * anchura
def calcular_perimetro(longitud, anchura):
    return 2 * (longitud + anchura)
try:
    longitud = float(input("Ingrese la longitud del rectángulo: "))
    anchura = float(input("Ingrese la anchura del rectángulo: "))

    validar_dimensiones(longitud, anchura)

    area = calcular_area(longitud, anchura)
    perimetro = calcular_perimetro(longitud, anchura)

    print(f"\n✅ Resultados:")
    print(f"Área: {area:.2f} unidades cuadradas")
    print(f"Perímetro: {perimetro:.2f} unidades")

except ValueError as ve:
    print(f"❌ Error de valor: {ve}")
except TypeError as te:
    print(f"❌ Error de tipo: {te}")
except Exception as e:
    print(f"❌ Ocurrió un error inesperado: {e}")
