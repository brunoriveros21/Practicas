
import random

# Definir los límites de los números permitidos
min_numero = 1
max_numero = 10



# Definir la cantidad de números que se deben generar
cantidad_numeros = 6

# Generar los números aleatorios
numeros_ganadores = random.sample(range(min_numero, max_numero + 1), cantidad_numeros)

# Ordenar los números de menor a mayor
numeros_ganadores.sort()

# Imprimir los números ganadores
print("Números ganadores:")
for numero in numeros_ganadores:
    print(numero)
