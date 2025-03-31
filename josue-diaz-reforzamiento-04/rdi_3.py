"""Convertir tu diccionario a una lista y mostrar en consola el tipo de datos
final que tiene."""

# Se crea el diccionario actualizado (tomado de la solución anterior)
persona = {
    "nombre": "Juan Perez",
    "salario": 2500.0,
    "dni": "12345678A"
}

# Se convierte el diccionario a una lista de tuplas
lista_persona = list(persona.items())

# Se muestra la lista y el tipo de dato final
print("Diccionario convertido a lista:")
print(lista_persona)
print("Tipo de datos final:", type(lista_persona))