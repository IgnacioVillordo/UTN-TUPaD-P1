# 1. Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
edad = int(input("Escriba su edad:"))
if edad >= 18:
    print("Es mayor de edad.")

# 2. Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.
nota = int(input("Escriba su nota:"))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# 3. Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por 
# en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un 
# número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.
num = int(input("Escriba un número:"))
if num % 2 == 0:
    print("Por favor, ingrese un número par.")
else:
    print("Ha ingresado un número par.")

# 4. Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
# *Niño/a: menor de 12 años.
# *Adolescente: mayor o igual que 12 años y menor que 18 años.
# *Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# *Adulto/a: mayor o igual que 30 años.

edad = int(input("Escriba su edad:"))
if(edad < 12):
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >=18 and edad < 30:
    print("Adulto/a joven")
elif edad >= 30:
    print("Adulto")

# 5. Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una 
# contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir 
# por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para 
# evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.

pw = input("Ingrese una contraseña")
if len(pw) >= 8 and len(pw) <=14:
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# 6. Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay 
# sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
import random
from statistics import mode, median, mean
numeros_aleatorios = [random.randint(1,100) for i in range(50)]
bmode = mode(numeros_aleatorios)
bmedian = median(numeros_aleatorios)
bmean = mean(numeros_aleatorios)
if bmean > median and median > mode:
    print("Sesgo positivo")
elif bmean < bmedian and bmedian < bmode:
    print("Sesgo negativo")
else:
    print("Sin sesgo")

# 7. Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación 
# al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

frase = input("Ingrese una frase o palabra:")
if frase[-1].lower in "aeiou":
    frase += "!"
else:
    pass
print(frase)

# 8. Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
#   1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#   2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#   3. Si quiere su nombre con la primera letra mayúscula. 
# Por ejemplo: Pedro. El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla.
nombre = input("Ingrese su nombre:")
eleccion = int(input("Ingrese la opcción que desee:\n1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.\n2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.\n3. Si quiere su nombre con la primera letra mayúscula."))
if eleccion == 1:
    print(nombre.upper())
elif eleccion == 2:
    print(nombre.lower())
elif eleccion == 3:
    print(nombre.title())

# 9. Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la 
# escala de Richter e imprima el resultado por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
# generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
# débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitud = float(input("Ingrese la magnitud del terremoto:"))
if magnitud < 3:
    print("Muy leve")
elif magnitud >= 4 and magnitud < 5:
    print("Leve")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte")
elif magnitud >= 7:
    print("Extremo")

#10. Utilizando la información aporta en la tabla sobre estaciones del año, escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), 
# qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio = input("Ingrese el en que hemisferio se encuentra (S/N)")
mes = int(input("Ingrese el mes (1-12):"))
dia = int(input("Ingrese el día del mes:"))
hemisferio = hemisferio.lower()

if hemisferio not in ('s','n'):
    print("Hemisferio inválido")
else:
    if (mes < 1 or mes > 12) or (dia < 1 or dia > 31):
        print("Fecha inválida")
    else:
        if (mes in [4, 6, 9, 11] and dia > 30) or (mes == 2 and dia > 28):
            print("Fecha inválida")
        else:
            if (mes == 12 and dia >= 21) or (mes <= 3 and dia <= 20):
                print("Invierno") if (hemisferio == "n") else print("Verano")
            elif (mes == 3 and dia >= 21) or (mes <= 6 and dia <= 20):
                print("Primavera") if (hemisferio == "n") else print("Otoño")
            elif (mes == 6 and dia >= 21) or (mes <= 9 and dia <= 20):
                print("Verano") if (hemisferio == "n") else print("Invierno")
            elif (mes == 9 and dia >= 21) or (mes <= 12 and dia <= 20):
                print("Otoño") if (hemisferio == "n") else print("Primavera")