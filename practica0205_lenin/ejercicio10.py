# Escribir un programa que almacene en una lista los siguientes precios,
# 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.

lista_precios = [50, 75, 46, 22, 80, 65, 8]
lista_precios.sort()

for precio in lista_precios:
    print(precio)
