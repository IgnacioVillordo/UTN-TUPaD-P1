# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
for i in range(101):
    print(i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.
num = int(input("Ingrese un número:"))
aux = 0
for i in range(len(str(num))):
    aux += 1
print(f"El número {num} tiene {aux} dígitos.")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))
num1 = min(num1, num2)
num2 = max(num1, num2)
suma = sum(range(num1 + 1, num2))
print(f"La suma de los números comprendidos entre {min(num1, num2)} y {max(num1, num2)} es {suma}")

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse 
# y mostrar el total acumulado cuando el usuario ingrese un 0.

aux = 0
num = -1
while num != 0:
    num = int(input("Ingrese un número: "))
    aux += num
print(f"La suma de todos los números ingresados es {aux}")

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random as random

print("||| ADIVINA EL NÚMERO |||")
numero = random.randint(0,9)
print(numero)
num = int(input("Ingresa un número: "))
cont = 0
while num != numero:
    num = int(input("Incorrecto, ingresa otro número: "))
    cont += 1
if cont == 0:
    print("Felicidades, has adivinado el número al primer intento.")
else:
    print(f"Felicidades, has adivinado el número en {cont} intentos.")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

for i in range(100, 0, -2):
    print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

num = int(input("Ingrese un número positivo: "))

while num < 0:
    num = int(input("Ingrese un número positivo: "))

for i in range(0, num, 2):
    print(i)

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son 
# pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor,
# pero debe estar preparado para procesar 100 números con un solo cambio).

positivos = 0
negativos = 0
cero = 0
for i in range(100):
    num = int(input("Ingrese un número: "))
    if num < 0:
        negativos += 1
    elif num > 0:
        positivos += 1
    else:
        cero += 1
print(f"La cantidad de negativos es {negativos}, la cantidad de positivos es {positivos} y la cantidad de 0 es {cero}")


# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar 
# el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).

aux = 0
cont = 0
for i in range(100):
    num = int(input("Ingrese un número: "))
    aux += num
    cont += 1
print(f"La media de los números ingresados es {aux/cont}")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 
# 547, el programa debe mostrar 745.

num = int(input("Ingrese un número: "))
aux = ""
# print(str(num)[::-1])
for i in range(len(str(num)), 0, -1):
    aux += str(num)[i - 1]
print(aux)