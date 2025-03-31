
# Lista con nombre, apellido y diferentes tipos de datos
lista_mixta = ["Josue", "Diaz", 25, 3.14, "Pythonauta", True, False, 100, 2.71]

# Lista con 6 números pares
lista_pares = [2, 4, 6, 8, 10, 12]

# Suma de ambas listas
lista_combinada = lista_mixta + lista_pares

# Mostrar las listas en pantalla
print("Lista Mixta:", lista_mixta)
print("Lista de Pares:", lista_pares)
print("Lista Combinada:", lista_combinada)

"""Comentario:
Cuando sumamos dos listas con el operador suma (+), los elementos 
no se combinan matemáticamente, sino que simplemente se concatenan 
en una sola lista, manteniendo el orden original. 
Como resultado, obtenemos una lista más grande que contiene todos 
los elementos de ambas listas.
"""