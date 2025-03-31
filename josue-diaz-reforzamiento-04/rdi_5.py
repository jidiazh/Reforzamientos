
"""Ingresar el nombre de tu carrera dentro de los valores que tienes en tu
diccionario. - Mostrar en consola los valores de tu carrera y nombre agregándolos a
una variable c/u """
datos = {
    "nombre": input("Ingresa tu nombre: "),
    "carrera": input("Ingresa el nombre de tu carrera: ")
}

# Asignar a variables separadas
nombre = datos["nombre"]
carrera = datos["carrera"]

# Mostrar en consola
print("Nombre:", nombre)
print("Carrera:", carrera)
