"""Crear un programa en Python donde tendrás una lista con 5 departamentos,
el programa te pedirá ingresar 2 departamentos el cual el segundo
departamento que ingreses sustituirá al primero de la lista. """
from numpy.ma.core import append

# Lista con 5 departamentos
departamentos = ["Lima", "Cusco", "Arequipa", "Piura", "Trujillo"]

# lista original
print("Lista original de departamentos:", departamentos)

# Pedir dos departamentos al usuario
dep_1 = input("Ingrese el primer departamento: ")
dep_2 = input("Ingrese el segundo departamento : ") #(sustituirá al primero de la lista)

departamentos.append(dep_1)

departamentos[0] = dep_2

# Mostrar la lista actualizada
print("Lista actualizada de departamentos:", departamentos)
