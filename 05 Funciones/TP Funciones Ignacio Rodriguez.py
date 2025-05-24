import math

def imprimir_hola_mundo():
    print("Hola Mundo!")

def saludar_usuario(nombre):
    print(f"Hola {nombre}!")
    
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

def calcular_area_circulo(radio):
    print(f"El área del círculo es {math.pi * radio ** 2}")
    
def calcular_perimetro_circulo(radio):
    print(f"El perímetro del círculo es {2 * math.pi * radio}")

def segundos_a_horas(segundos):
    return segundos/3600

def tabla_multiplicar(numero):
    for i in range(0, 11):
        print(f"{i} × {numero} = {i*numero}")

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return suma, resta, multiplicacion, division

def calcular_imc(peso, altura):
    return peso / ((altura / 100) ** 2)

def celsius_a_fahrenheit(celsius):
    print(f"{celsius}°C es igual a {(celsius * 9/5) + 32}°F")

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

imprimir_hola_mundo()
nombre = input("Ingrese su nombre: ")
saludar_usuario(nombre)

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su lugar de residencia: ")
informacion_personal(nombre, apellido, edad, residencia)

radio = int(input("Ingrese el radio del círculo: "))
calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)

segundos = int(input("Ingrese la cantidad de segundos: "))
print(f"{segundos} segundos es igual a {segundos_a_horas(segundos)} horas")

numero = int(input("Ingrese un número para mostrar su tabla de multiplicar: "))
tabla_multiplicar(numero)

print(operaciones_basicas(10, 5))
peso = int(input("Ingrese su peso en kg: "))
altura = int(input("Ingrese su altura en cm: "))
print(f"Su IMC es {calcular_imc(peso, altura)}")


celsius = float(input("Ingrese la temperatura en grados Celsius: "))
celsius_a_fahrenheit(celsius)


a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))
print(f"El promedio de los números {a}, {b}, {c} es {calcular_promedio(a, b, c)}")