"""Crea correctamente un diccionario con los campos de: nombre, edad, salario
y edad.
Convierte tu diccionario finalmente a una lista y muestra el resultado en la
terminal."""

persona = {"nombre": "Juan Perez", "edad": 30,"salario": 2500.0}

# Convertir el diccionario a una lista de tuplas (clave, valor)
lista_persona = list(persona.items())

# Mostrar el diccionario y la lista resultante en la terminal
print("Diccionario original:")
print(persona)
print("Diccionario convertido a lista (lista de tuplas):")
print(lista_persona)