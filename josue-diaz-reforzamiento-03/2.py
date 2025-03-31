"""Devuelve la cantidad de veces que se repite un curso que hayas llevado en
pregrado (agregarlos previamente a la lista con un mínimo de 5 cursos) luego
mostrarla, finalmente elimina el segundo ítem de la lista usando debidamente
su índice y mostrar en consola tu lista actualizada
"""
# Lista con cursos que he llevado en pregrado
cursos = ["Mecánica Clásica", "Cálculo III", "Programación", "Química", "Mecánica Clásica", "Biología", "Mecánica Clásica"]

print("Lista de cursos:", cursos)

# Contar cuántas veces se repite un curso específico (ejemplo: "Física")
curso_repetido = "Mecánica Clásica"
cantidad_repeticiones = cursos.count(curso_repetido)

# Mostrar cuántas veces se repite el curso
print("El curso '{}' se repite {} veces.".format(curso_repetido,cantidad_repeticiones))

# Eliminar el segundo curso de la lista (índice 1)
del cursos[1]

# Mostrar la lista actualizada
print("Lista actualizada:", cursos)
