"""Realizar un programa donde se ingresarán por consola los nombres de los
alumnos (indicar previamente la cantidad de alumnos a ingresar) de un curso
y las notas de c/u. Guardarás la información en un diccionario donde las claves
serán los nombres de c/u de estos alumnos y sus valores serán las notas de
esto alumnos.
Finalmente mostrarás los alumnos con sus notas en un mensaje similar a
“Pedro tiene la nota de 15” y también la media de todas las notas. """

# Solicitar la cantidad de alumnos a ingresar
cantidad = int(input("Ingresa la cantidad de alumnos: "))

# Inicializar el diccionario para almacenar los datos de alumnos y notas
alumnos = {}

# Bucle para ingresar el nombre y la nota de cada alumno
for i in range(cantidad):
    nombre = input(f"Ingrese el nombre del alumno {i + 1}: ")
    # Se lee la nota y se convierte a float (o int, según se requiera)
    nota = float(input("Ingrese la nota de {}:".format(nombre)))
    alumnos[nombre] = nota

print("Notas de los alumnos:")
# impresion de la información de cada alumno en el formato indicado
for nombre, nota in alumnos.items():
    print("{} tiene la nota de {}".format(nombre,nota))

# Calculo de la media de las notas
if cantidad > 0:
    media = sum(alumnos.values()) / cantidad
    print("La media de las notas es: {:.2f}".format(media))

else:
    print("No se ingresaron alumnos.")
