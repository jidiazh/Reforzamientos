"""Agregar 5 Objetos nuevos a tu lista (append) y quitar 2 elementos de esta
lista por valor. Mostrar la lista final en la terminal.
Obtén también la cantidad total ítems que tienes en tu lista ya creada para
agregar este valor a tu lista y mostrar también el resultado final de cantidad
total de elemento y la lista actualizada en consola."""

# Lista inicial con algunos países
mi_lista = ["Perú", "Argentina", "Brasil", "Chile", "Ecuador"]

# Agregamos 5 países nuevos a la lista
mi_lista.append("Colombia")
mi_lista.append("México")
mi_lista.append("España")
mi_lista.append("Italia")
mi_lista.append("Japón")

# Eliminarción de 2 países por su valor
mi_lista.remove("Brasil")
mi_lista.remove("Ecuador")

print("Lista final:", mi_lista)

cantidad_elementos = len(mi_lista)

# Agregamos la cantidad actualizada de elementos a la lista
mi_lista.append(cantidad_elementos)

# Mostrar la lista final y la cantidad total
print("Lista final:", mi_lista)
print("Cantidad total de elementos:", cantidad_elementos)
