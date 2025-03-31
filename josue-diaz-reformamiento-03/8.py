"""
Escribir un programa donde ingresará 8 nombres de países. Se quiere
hacer un clon de la lista, esta copia se le eliminará el primer y penúltimo
valor, mostrar finalmente el tamaño de la lista modificada, la lista original
y todos sus elementos de la lista modificada.
"""


# Ingresar 8 nombres de países en la lista
paises = ["Perú", "Argentina", "Brasil", "Chile", "México", "España", "Francia", "Japón"]

# Hacer una copia de la lista
paises_modificados = paises.copy()

# Eliminar el primer elemento
paises_modificados.pop(0)

# Eliminar el penúltimo elemento
paises_modificados.pop(-2)

# Mostrar resultados
print("Lista original:", paises)
print("Lista modificada:", paises_modificados)
print("Tamaño de la lista modificada:", len(paises_modificados))
