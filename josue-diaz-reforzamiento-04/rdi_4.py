"""Crear un diccionario con 6 departamentos en el país. - Borrar cualquier departamento, usando la palabra reservada del. - Actualizar el penúltimo departamento por otro. - Comprobar que no existe este departamento borrado dentro del
diccionario. """

# Crear un diccionario con 6 departamentos del país.
departamentos = {
    "Departamento 1": "Ayacucho",
    "Departamento 2": "Cuzco",
    "Departamento 3": "Lima",
    "Departamento 4": "Abancay",
    "Departamento 5": "La libertad",
    "Departamento 6": "Lambayeque"
}

print("Diccionario original:")
print(departamentos)


# 1. Borrar cualquier departamento usando la palabra reservada 'del'.
# Por ejemplo, eliminamos "Departamento C":
del departamentos["Departamento 3"]

print("Diccionario tras borrar 'Departamento 3':")
print(departamentos)


# 2. Actualizar el penúltimo departamento por otro.
# Convertimos las claves a una lista (los diccionarios mantienen el orden de inserción en Python 3.7+)
claves = list(departamentos.keys())
# Obtenemos el penúltimo elemento:
penultimo = claves[-2]
# Actualizamos su valor o incluso su nombre; en este ejemplo actualizaremos su valor:
departamentos[penultimo] = "Nuevo Valor para Penúltimo Departamento"

print("Diccionario tras actualizar el penúltimo departamento:")
print(departamentos)
print()

# 3. Comprobar que no existe el departamento borrado ("Departamento C")
if "Departamento C" not in departamentos:
    print("El departamento 'Departamento 3' ha sido borrado exitosamente.")
else:
    print("El departamento 'Departamento 3' sigue existiendo.")

