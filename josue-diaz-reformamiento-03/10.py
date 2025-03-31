"""
Tienes una lista con 7 diferentes nombres de BD relacionales. De la cual 3
BDs estarán repetidas adrede (en posiciones no consecutivas), sacar la
base de datos repetidas uno por valor y le otro por índice.
Finalmente mostrar la lista actualizada en consola.
"""

bd_relacionales = ["MySQL", "PostgreSQL", "SQL Server", "Oracle", "MySQL", "SQLite", "PostgreSQL"]

bd_relacionales.remove("MySQL")

bd_relacionales.pop(5)

print("Lista actualizada:", bd_relacionales)
