"""Ingresar por consola el tamaño de una lista, luego empezarás a ingresar los
datos mediante consola también (5 compañías relacionadas con al mundo de
TI) y harás una copia donde adrede agregarás nombres que estarán
repetidos (mediante consola) para que finalmente muestres otra lista donde
solo se mostrará los nombres no repetidos y también la lista inicial
"""

# Solicitar el tamaño de la lista
tamanio = int(input("Ingrese el tamaño de la lista de compañías : "))

# Ingresar datos para la lista original
lista_original = []
print("Ingrese los nombres de las compañías de TI:")
for i in range(tamanio):
    compania = input(f"Compañía {i+1}: ")
    lista_original.append(compania)

# Mostrar la lista original
print("Lista original:")
print(lista_original)

# Crear una copia donde se agregarán nombres adicionales (algunos repetidos)
lista_con_repetidos = lista_original.copy()
print("Ingrese nombres adicionales (pueden estar repetidos) para la copia de la lista.")
print("Escriba 'fin' para terminar de ingresar nombres adicionales.")
while True:
    nuevo_nombre = input("Nuevo nombre: ")
    if nuevo_nombre.lower() == 'fin':
        break
    lista_con_repetidos.append(nuevo_nombre)

# Mostrar la lista con nombres repetidos
print("Lista con nombres adicionales (con posibles repeticiones):")
print(lista_con_repetidos)

# Crear una lista solo con nombres no repetidos (únicos)
# Se mantiene el orden de aparición en la lista original
lista_unicos = []
for nombre in lista_con_repetidos:
    if nombre not in lista_unicos:
        lista_unicos.append(nombre)

print("Lista final con nombres únicos:")
print(lista_unicos)
