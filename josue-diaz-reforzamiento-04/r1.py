"""Escribir un programa donde ingresarás el tamaño de la lista mediante
consola, este tamaño servirá para ingresar una cantidad X de nombres de
alumnos. Ingresarás los nombres mediante consola también.
Se quiere mostrar finalmente el tamaño de la lista y todos los nombres de
la lista que fueron ingresados. """

# Pedimos el tamaño de la lista
tam_lista = int(input("Ingrese la cantidad de alumnos: "))

# Crear una lista vacía para almacenar los nombres
nombres = []

# Usar un bucle for para ingresar los nombres
for i in range(tam_lista):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    nombres.append(nombre)

# imprimir el tamaño de la lista y los nombres ingresados
print("Tamaño de la lista:", len(nombres))
print("Nombres de los alumnos:", nombres)
