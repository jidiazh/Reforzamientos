"""Crea una siguiente lista vacía y agregue ítems a partir de variables (los cuales
tendrán los siguientes tipos de datos: 3 floats, 3 ints y 3 strings) (append).
Sumar las dos listas creadas anteriormente y mostrar el resultado en consola. """

# Lista de cursos del ejercicio anterior
cursos = ["Mecánica Clásica", "Cálculo III", "Programación", "Química", "Mecánica Clásica", "Biología", "Mecánica Clásica"]

# Crear una nueva lista vacía
nueva_lista = []

# Variables solicitadas
float1 = 3.14
float2 = 2.71
float3 = 1.618
int1 = 10
int2 = 20
int3 = 30
str1 = "Python"
str2 = "Java"
str3 = "C++"

# Agregar los valores a la nueva lista usando append()
nueva_lista.append(float1)
nueva_lista.append(float2)
nueva_lista.append(float3)
nueva_lista.append(int1)
nueva_lista.append(int2)
nueva_lista.append(int3)
nueva_lista.append(str1)
nueva_lista.append(str2)
nueva_lista.append(str3)

# Sumar las dos listas
lista_final = cursos + nueva_lista

# Mostrar la lista final en consola
print("Lista combinada:", lista_final)
