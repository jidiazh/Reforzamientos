"""
Ingresar por consola 4 números mediante consola, crear un diccionario
donde los ‘key’ serán los números indicados y los valores serán los cubos de
las estos keys. Mostrar finalmente este diccionario
"""
# diccionario vacío para almacenar los números y sus cubos
cubos = {}

# Se solicita ingresar 4 números por consola
print("Ingresa 4 números:")
for i in range(4):
    # Convertir la entrada a entero (puedes usar float() si lo prefieres)
    num = int(input(f"Número {i + 1}: "))
    # Calcular el cubo del número y asignarlo como valor en el diccionario
    cubos[num] = num ** 3

# imprimir el diccionario resultante
print("Diccionario de números y sus cubos:")
print(cubos)