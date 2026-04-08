
# 13 Crear un programa que:
# Calcule cuantos meses viviste aproximadamente.
# Calcula tu edad dentro de 10 años.
# Calcula el doble de tu altura.
# Imprime los resultados con mensajes descriptivos.

edad = int(input("Ingrese su edad: "))
meses_vida = edad * 12
edad10anos = edad + 10
altura = float(input("Ingrese su altura en metros: "))
altura_doble = 2 * altura

print(f"La edad del usuario es: {edad}")
print(f"Los meses de vida del usuario son: {meses_vida}")
print(f"La edad del usuario en 10 años sera de: {edad10anos}")
print(f"La altura del usuario es: {altura}")
print(f"El doble de la altura del usuario es: {altura_doble}")