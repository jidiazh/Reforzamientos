"""
Crear una lista (entre floats y bools, 6 elementos mínimo) donde imprimas el
penúltimo y antepenúltimo valor (por índice). Reconocer cada uno de los tipos
de datos en esta lista creada y mostrar los resultados en consola
"""
# Lista con floats y booleanos
mi_lista = [3.14, True, 9.81, False, 2.71, True, 6.28]


# Mostrar los valores
print("Penúltimo valor:", mi_lista[-2])
print("Antepenúltimo valor:", mi_lista[-3])



# Reconocer el tipo de dato de cada elemento en la lista
print("\nTipos de datos en la lista:")
for elemento in mi_lista:
    print(f"Valor: {elemento}, Tipo: {type(elemento)}")
