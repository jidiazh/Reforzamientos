"""
Crea una lista vacía, luego ingresa sus valores (10 valores numéricos) y
finalmente muestra la suma y la media de los números ingresado insertados en
la terminal
"""
# Lista vacía
numeros = []

# Ingresamos 10 valores numéricos
numeros.extend([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# Calculamos la suma de los números
suma_total = sum(numeros)

# Calcular la media (promedio)
media = suma_total / len(numeros)

# Mostrar resultados
print("Lista de números:", numeros)
print("Suma de los números:", suma_total)
print("Media de los números:", media)
