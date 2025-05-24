def factorial(n):
    if n == 0 or n == 1:
        print(f"{n}! = 1")
        return 1
    else:
        fact = n * factorial(n - 1)
        print(f"{n}! = {fact}")
        return fact
    
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
            
def potencia_recursiva(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia_recursiva(base, exponente - 1)
    
def decimal_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

num = int(input("Ingrese un número para calcular su factorial: "))
factorial(num)

num = int(input("Ingrese un número para calcular la sucesión de Fibonacci: "))
for i in range(num + 1):
    print(f"Fibonacci({i}) = {fibonacci(i)}")

base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))
print(f"{base}^{exponente} = {potencia_recursiva(base, exponente)}")

num = int(input("Ingrese un número decimal para convertir a binario: "))
print(f"El número {num} en binario es: {decimal_a_binario(num)}")