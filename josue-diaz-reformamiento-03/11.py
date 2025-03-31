"""
Ingresar compañías relacionadas con al mundo de TI, copia los elementos
de la lista en otra lista pero estarán orden inverso, y muestra sus
elementos por la terminal y la lista original también.
"""

# Lista de compañías de tecnología
companias_ti = ["Microsoft", "Google", "Apple", "Amazon", "Meta", "IBM", "Intel"]

# Hacer una copia de la lista original
companias_invertidas = companias_ti.copy()

# Invertir el orden de la lista copiada
companias_invertidas.reverse()

# Mostrar resultados
print("Lista original:", companias_ti)
print("Lista en orden inverso:", companias_invertidas)

