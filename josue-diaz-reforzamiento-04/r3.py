"""Tienes una lista con 5 nombres de estudiantes. Crear un programa que te
pedirá ingresar el nombre de un estudiante, la cuál será eliminada de lista
inicial en caso que no exista en la lista mostrar un mensaje donde indique
que no se encuentre en la lista y esta será agregada a la lista.
Finalmente mostrar la lista actualizada en consola."""




# Lista con 5 nombres de estudiantes
estudiantes = ["Arian", "Carlos", "Mauricio", "María", "Pedro"]

# Mostrar la lista original
print("Lista original de estudiantes:", estudiantes)

# Pedir el nombre del estudiante
nombre = input("Ingrese el nombre del estudiante que desea eliminar o agregar: ")

# Verificar si el nombre está en la lista
if nombre in estudiantes:
    # Si el nombre está en la lista, lo eliminamos
    estudiantes.remove(nombre)
    print("El estudiante {} ha sido eliminado de la lista.".format(nombre))
else:
    # Si el nombre no está en la lista, lo agregamos
    estudiantes.append(nombre)
    print("El estudiante {} no estaba en la lista, se ha agregado.".format(nombre))

# Mostrar la lista actualizada
print("Lista actualizada de estudiantes:", estudiantes)
