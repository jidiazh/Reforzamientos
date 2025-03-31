
"""Agrega un nuevo key llamado “dni” con su respectivo valor y luego mostrar
el valor del salario y DNI en consola. También elimina el key edad de tu
diccionario, incluyendo su valor. Mostrar finalmente el diccionario
actualizado. """
# Se crea el diccionario inicial usando un literal
persona = {
    "nombre": "Juan Perez",
    "edad": 30,
    "salario": 2500.0
}

# Se agrega un nuevo key "dni" con su valor
persona["dni"] = "12345678A"

# Se muestran el valor del salario y el DNI
print("Salario:", persona["salario"])
print("DNI:", persona["dni"])

# Se elimina el key "edad"
persona.pop("edad", None)  # Se utiliza pop con un valor por defecto en caso de que la clave no exista

# Se muestra el diccionario actualizado
print("Diccionario actualizado:")
print(persona)
