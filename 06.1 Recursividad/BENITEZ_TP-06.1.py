def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)

def fibonacci(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci(posicion - 1) + fibonacci(posicion - 2) 

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

def decimal_a_binario(numero):
    if numero == 0:
        return ""
    else:
        return decimal_a_binario(numero // 2) + str(numero % 2)
    
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    else:
        return palabra[0] == palabra[-1] and es_palindromo(palabra[1:-1])

def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return suma_digitos(n // 10) + (n % 10)

def contar_bloques(cantidad_de_bloques):
    if cantidad_de_bloques == 1:
        return 1
    else:
        return cantidad_de_bloques + contar_bloques(cantidad_de_bloques - 1)

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        ultimo_digito = numero % 10
        return contar_digito((numero // 10), digito) + (1 if ultimo_digito == digito else 0)

def mostrar_menu():
    print("\nMenú de Ejercicios:\n")
    print("1. Calcular factorial de un número")
    print("2. Calcular serie de Fibonacci")
    print("3. Calcular potencia de un número")
    print("4. Convertir número decimal a binario")
    print("5. Verificar si una palabra es palíndromo")
    print("6. Sumar dígitos de un número")
    print("7. Contar bloques en una pirámide")
    print("8. Contar dígitos en un número")
    print("\n0. Salir\n")

def main():
    continuar = True
    while continuar:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opción: "))
            match opcion:
                case 0:
                    continuar = False
                case 1:
                    print("\nEjercicio 1: Calcular factorial de los números (entre 1 y el número ingresado).\n")
                    try:
                        numero = int(input("Ingrese un número: "))
                        for i in range(1, numero + 1):
                            print(f"El factorial de {i} es {factorial(i)}")
                    except ValueError:
                        print("Por favor, ingrese un número válido.")
                case 2:
                    print("\nEjercicio 2: Calcular serie de Fibonacci.\n")
                    try:
                        posicion = int(input("Ingrese la posición en la serie de Fibonacci: "))
                        for i in range(posicion + 1):
                            print(fibonacci(i), end=" ")
                    except ValueError:
                        print("Por favor, ingrese un número válido.")
                case 3:
                    print("Ejercicio 3: Calcular potencia de un número")
                    try:
                        base = int(input("Ingrese la base: "))
                        exponente = int(input("Ingrese el exponente: "))
                        print(f"{base} elevado a {exponente} es {potencia(base, exponente)}")
                    except ValueError:
                        print("Por favor, ingrese números válidos.")
                case 4:
                    print("Ejercicio 4: Convertir número decimal a binario")
                    try:
                        numero = int(input("Ingrese un número decimal: "))
                        if numero == 0:
                            print("El número binario de 0 es 0")
                        else:
                            print(f"El número binario de {numero} es {decimal_a_binario(numero)}")
                    except ValueError:
                        print("Por favor, ingrese un número válido.")
                case 5:
                    print("Ejercicio 5: Verificar si una palabra es palíndromo")
                    palabra = input("Ingrese una palabra: ").lower()
                    if es_palindromo(palabra):
                        print(f"'{palabra}' es un palíndromo.")
                    else:
                        print(f"'{palabra}' no es un palíndromo.")
                case 6:
                    print("Ejercicio 6: Sumar dígitos de un número")
                    try:
                        numero = int(input("Ingrese un número entero positivo: "))
                        if numero < 0:
                            print("Por favor, ingrese un número no negativo.")
                            return
                        print(f"La suma de los dígitos de {numero} es {suma_digitos(numero)}")
                    except ValueError:
                        print("Por favor, ingrese un número válido.")
                case 7:
                    print("Ejercicio 7: Contar bloques en una pirámide")
                    try:
                        n = int(input("Ingrese el número de bloques en el nivel más bajo: "))
                        if n < 1:
                            print("Por favor, ingrese un número positivo.")
                            return
                        print(f"El total de bloques necesarios es {contar_bloques(n)}")
                    except ValueError:
                        print("Por favor, ingrese un número válido.")
                case 8:
                    print("Ejercicio 8: Contar dígitos en un número")
                    try:
                        numero = int(input("Ingrese un número entero positivo: "))
                        digito = int(input("Ingrese el dígito a contar (entre 0 y 9): "))
                        if numero < 0 or digito < 0 or digito > 9:
                            print("Por favor, ingrese números válidos.")
                            return
                        print(f"El dígito {digito} aparece {contar_digito(numero, digito)} veces en {numero}")
                    except ValueError:
                        print("Por favor, ingrese números válidos.")
                case _:
                    print("Opción no válida")
        except ValueError:
            print("Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()