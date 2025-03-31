"""
Crear un programa en Python donde tendrás una lista con 5
departamentos, ingresarás 2 departamentos adicionales por posición, el
cual el segundo departamento estará en la posición ‘1’ y el primero en
penúltimo lugar, finalmente mostrar la lista original y la lista actualizada
en terminal
"""


# Lista inicial con 5 departamentos
departamentos = ["Lima", "Cusco", "Arequipa", "Piura", "Trujillo"]

# Hacer una copia de la lista original para mostrarla después
departamentos_original = departamentos.copy()

# Insertar 2 nuevos departamentos en posiciones específicas
departamentos.insert(1, "Tacna")  # Segundo departamento en la posición 1
departamentos.insert(-1, "Ica")   # Primer departamento en la penúltima posición

# Mostrar resultados
print("Lista original:", departamentos_original)
print("Lista actualizada:", departamentos)
