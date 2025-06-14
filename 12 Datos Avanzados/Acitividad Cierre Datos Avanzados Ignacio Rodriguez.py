# 1) Dado el diccionario precios_frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
print(precios_frutas)

# Añadir las siguientes frutas con sus respectivos precios:
# - Naranja = 1200
# - Manzana = 1500
# - Pera = 2300
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print(precios_frutas)

# 2) Actualizar los precios de las siguientes frutas:
# - Banana = 1330
# - Manzana = 1700
# - Melón = 2800
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
print(precios_frutas)

# 3) Crear una lista que contenga únicamente las frutas sin los precios.
lista_frutas = list(precios_frutas.keys())
print("Lista de frutas:", lista_frutas)

# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# - Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# - Luego, pedí un nombre y mostrale el número asociado, si existe.
contactos = {}
for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i + 1}: ")
    numero = input(f"Ingrese el número de teléfono de {nombre}: ")
    contactos[nombre] = numero 
nombre_consulta = input("Ingrese el nombre del contacto que desea consultar: ")
if nombre_consulta in contactos:
    print(f"El número de teléfono de {nombre_consulta} es: {contactos[nombre_consulta]}")

# 5) Solicita al usuario una frase e imprime:
# - Las palabras únicas (usando un set).
# - Un diccionario con la cantidad de veces que aparece cada palabra.

frase = input("Ingrese una frase: ")
palabras_unicas = set(frase.split())
cantidad_palabras = {}
for palabra in frase.split():
    cantidad_palabras[palabra] = cantidad_palabras.get(palabra, 0) + 1
print("Palabras únicas:", palabras_unicas)
print("Cantidad de veces que aparece cada palabra:", cantidad_palabras)

# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.

alumnos = {}
for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i + 1}: ")
    notas = {}
    alumnos[nombre] = notas
for nombre in alumnos:
    notas = []
    for j in range(3):
        nota = float(input(f"Ingrese la nota {j + 1} de {nombre}: "))
        notas.append(nota)
    alumnos[nombre] = notas
for nombre, notas in alumnos.items():
    promedio = sum(notas) / 3
    print(f"El promedio de {nombre} es: {promedio:.2f}")

# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
# - Mostrá los que aprobaron ambos parciales.
# - Mostrá los que aprobaron solo uno de los dos.
# - Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).
parcial_1 = {4, 2, 9, 3, 7}
parcial_2 = {4, 5, 2, 7, 1}
aprobados_ambos = parcial_1.intersection(parcial_2)
aprobados_uno = parcial_1.symmetric_difference(parcial_2)
aprobados_total = parcial_1.union(parcial_2)
print("Aprobados en ambos parciales:", aprobados_ambos)
print("Aprobados en solo uno de los parciales:", aprobados_uno)
print("Total de estudiantes que aprobaron al menos un parcial:", aprobados_total)

# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
# - Consultar el stock de un producto ingresado.
# - Agregar unidades al stock si el producto ya existe.
# - Agregar un nuevo producto si no existe.

productos_stock = {}
def consultar_stock(producto):
    return productos_stock.get(producto, "Producto no encontrado.")
def agregar_stock(producto, unidades):
    productos_stock[producto] = productos_stock.get(producto, 0) + unidades

def agregar_producto(producto, unidades):
    productos_stock[producto] = unidades

while True:
    accion = int(input("Ingrese un número para continuar:\n"
    "1) Ver producto.\n"
    "2) Agregar stock.\n"
    "3) Agregar producto.\n"
    "4) Salir."))
    if accion == 1:
        producto = input("Ingrese el nombre del producto a consultar: ")
        print(f"{producto}: {consultar_stock(producto)}")
    elif accion == 2:
        producto = input("Ingrese el nombre del producto a agregar unidades: ")
        unidades = int(input("Ingrese la cantidad de unidades a agregar: "))
        agregar_stock(producto, unidades)
        print(f"Stock actualizado de {producto}: {productos_stock[producto]}")
    elif accion == 3:
        producto = input("Ingrese el nombre del nuevo producto: ")
        unidades = int(input("Ingrese la cantidad de unidades del nuevo producto: "))
        agregar_producto(producto, unidades)
        print(f"Producto {producto} agregado con stock inicial de {unidades}.")
    elif accion == 4:
        print("Saliendo del programa.")
        break
    else:
        print("Acción no reconocida. Intente nuevamente.")

# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Permití consultar qué actividad hay en cierto día y hora
agenda = {
    ('Lunes', '10:00'): 'Reunión con el equipo',
    ('Martes', '15:00'): 'Clase de inglés'
}
def consultar_evento(dia, hora):
    return agenda.get((dia, hora), "No hay evento programado.")

while True:
    accion = int(input("Ingrese un número para continuar:\n"
    "1) Consultar evento.\n"
    "2) Salir."))
    if accion == 1:
        dia = input("Ingrese el día del evento a consultar: ")
        hora = input("Ingrese la hora del evento a consultar: ")
        print(f"Evento programado para {dia} a las {hora}: {consultar_evento(dia, hora)}")
    elif accion == 2:
        print("Saliendo de la agenda.")
        break
    else:
        print("Acción no reconocida. Intente nuevamente.")

# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
# - Las capitales sean las claves.
# - Los países sean los valores.

original = {
    'Argentina': 'Buenos Aires',
    'Brasil': 'Brasilia',
    'Chile': 'Santiago',
    'Bolivia': 'Sucre',
    'Uruguay': 'Montevideo',
    'Paraguay': 'Asunción',
    'Perú': 'Lima'
}
invetido = {}
for pais, capital in original.items():
    invetido[capital] = pais
print("Diccionario original (países como claves):", original)
print("Diccionario invertido (capitales como claves):", invetido)