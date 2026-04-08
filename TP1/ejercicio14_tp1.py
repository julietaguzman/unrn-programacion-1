
# 14 Crear un programa que:
# Cree una variable saludo que diga: "Hola <tu nombre>".
# Cree otra variable que repita el saludo tres veces.
# Cuente cuantas letras tiene tu nombre usando len().

nombre = input("Ingrese su nombre: ")
saludo = f"Hola {nombre} "
repetir = 3 * saludo

print(f"El saludo es {saludo}")
print(f"El saludo repetido tres veces es: {repetir}")
print(f"Cantidad de letras del nombre: {len(nombre)}")
