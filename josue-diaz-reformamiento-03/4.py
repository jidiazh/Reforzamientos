"""Crea dos listas (una de datos string y la otra de datos numéricos) para luego
usar los métodos de orden (los elementos tienen que estar desordenados),
mostrar las listas antes y después de aplicarle los métodos de orden """

# Lista de ciudades desordenadas
ciudades = ["Londres", "Buenos Aires", "Tokio", "Madrid", "París", "Sídney"]

# Lista de edades desordenadas
edades = [34, 18, 25, 42, 29, 37]

# Mostrar listas antes del ordenamiento
print("Lista de ciudades antes de ordenar:", ciudades)
print("Lista de edades antes de ordenar:", edades)

# Ordenar ambas listas
ciudades.sort()  # Orden alfabético
edades.sort()  # Orden numérico ascendente

# Mostrar listas después del ordenamiento
print("Lista de ciudades después de ordenar:", ciudades)
print("Lista de edades después de ordenar:", edades)

