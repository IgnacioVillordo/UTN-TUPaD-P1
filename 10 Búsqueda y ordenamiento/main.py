import math
import time

def llega(trenes, velocidad, hora):
    tiempo = 0.0
    for i in range(0, len(trenes) - 1):
        tiempo += math.ceil(trenes[i] / velocidad)  
    tiempo += trenes[-1] / velocidad  
    return tiempo <= hora

def calcularVelocidadBinaria(trenes, hora):
    izquierda = 1
    derecha = 10000000
    resultado = -1
    while izquierda <= derecha:
        medio = izquierda + (derecha - izquierda) // 2
        if llega(trenes, medio, hora):
            resultado = medio
            derecha = medio - 1
        else:
            izquierda = medio + 1
    return resultado

def calcularVelocidadLineal(trenes, hora):
    velocidad = 1
    while velocidad <= 10000000:
        if llega(trenes, velocidad, hora):
            return velocidad
        velocidad += 1
    return -1

time_start = time.perf_counter()
print(f"Caso de prueba 1: {calcularVelocidadBinaria([1, 3, 2], 6.0)} || resultado esperado = 1")
print(f"Caso de prueba 2: {calcularVelocidadBinaria([1, 3, 2], 2.7)} || resultado esperado = 3")
print(f"Caso de prueba 3: {calcularVelocidadBinaria([1, 1, 100000], 0.5)} || resultado esperado = -1")
print(f"Caso de prueba 4: {calcularVelocidadBinaria([100], 1.0)} || resultado esperado = 100")
print(f"Caso de prueba 5: {calcularVelocidadBinaria([5, 5, 5], 3.0)} || resultado esperado = 5")
print(f"Caso de prueba 6: {calcularVelocidadBinaria([1, 1, 1], 3.0)} || resultado esperado = 1")
print(f"Caso de prueba 7: {calcularVelocidadBinaria([10, 20, 30], 6.0)} || resultado esperado = 10")
print(f"Caso de prueba 8: {calcularVelocidadBinaria([10, 20, 30], 5.5)} || resultado esperado = 12")
print(f"Caso de prueba 9: {calcularVelocidadBinaria([1000000, 1000000], 2.0)} || resultado esperado = 1000000")
print(f"Caso de prueba 10: {calcularVelocidadBinaria([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 10.0)} || resultado esperado = 1")

time_end = time.perf_counter()
print(f"Tiempo de ejecución binaria: {time_end - time_start:.6f} segundos")

time_start = time.perf_counter()
print(f"Caso de prueba 1: {calcularVelocidadLineal([1, 3, 2], 6.0)} || resultado esperado = 1")
print(f"Caso de prueba 2: {calcularVelocidadLineal([1, 3, 2], 2.7)} || resultado esperado = 3")
print(f"Caso de prueba 3: {calcularVelocidadLineal([1, 1, 100000], 0.5)} || resultado esperado = -1")
print(f"Caso de prueba 4: {calcularVelocidadLineal([100], 1.0)} || resultado esperado = 100")
print(f"Caso de prueba 5: {calcularVelocidadLineal([5, 5, 5], 3.0)} || resultado esperado = 5")
print(f"Caso de prueba 6: {calcularVelocidadLineal([1, 1, 1], 3.0)} || resultado esperado = 1")
print(f"Caso de prueba 7: {calcularVelocidadLineal([10, 20, 30], 6.0)} || resultado esperado = 10")
print(f"Caso de prueba 8: {calcularVelocidadLineal([10, 20, 30], 5.5)} || resultado esperado = 12")
print(f"Caso de prueba 9: {calcularVelocidadLineal([1000000, 1000000], 2.0)} || resultado esperado = 1000000")
print(f"Caso de prueba 10: {calcularVelocidadLineal([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 10.0)} || resultado esperado = 1")

time_end = time.perf_counter()
print(f"Tiempo de ejecución lineal: {time_end - time_start:.6f} segundos")