"""Crear una agenda basada en un diccionario donde los key serán los nombres
de las personas y sus “values” serán los números de teléfono de c/u.
Ingresarás por consola el nombre y el número de cada persona que serán
registrados en la agenda.
El programa también te permitirá buscar por nombre en el diccionario en caso
no exista mostrar un mensaje de “No se encuentra registrado en la agenda” """

# Se crea un diccionario vacío para la agenda.
agenda = {}

# Se solicita la cantidad de contactos a registrar.
cantidad = int(input("Ingrese la cantidad de contactos a registrar: "))

# Ingresar por consola cada nombre y teléfono y registrarlos en la agenda.
for i in range(cantidad):
    nombre = input("Ingrese el nombre del contacto {}: ".format(i + 1))
    telefono = input("Ingrese el número de teléfono de {}: ".format(nombre))
    agenda[nombre] = telefono

# Mostrar la agenda completa.
print("Agenda actual:")
for nombre, telefono in agenda.items():
    print("{}: {}".format(nombre, telefono))

# Búsqueda de un contacto por nombre.
busqueda = input("Ingrese el nombre a buscar en la agenda: ")
if busqueda in agenda:
    print("El número de teléfono de {} es {}".format(busqueda, agenda[busqueda]))
else:
    print("No se encuentra registrado en la agenda.")
