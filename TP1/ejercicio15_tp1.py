
# Parte 3: Un programa de presentación
# 15 Cree un programa de presentación en un archivo llamado tp1.py defina las siguientes variables:
# Una variable con tu nombre.
# Una variable con tu edad.
# Una variable con tu altura aproximada en metros.
# Una variable booleana que indica si te gusta programar.
# Una variable que, a partir del año actual y tu edad, calcula tu año de nacimiento aproximado.
# Luego, imprime toda esa información utilizando print().

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
altura = float(input("Ingrese su altura en metros: "))
me_gusta_programar = True
actual = int((input("Ingrese el año actual: ")))

ano_nacimiento = actual - edad

print(f"Mi nombre es: {nombre}")
print(f"Mi edad es: {edad}")
print(f"Mi altura es: {altura}")
print(f"Me gusta programar: {me_gusta_programar}")
print(f"Estamos en el año: {actual}")
print(f"Yo naci en el año: {ano_nacimiento}")