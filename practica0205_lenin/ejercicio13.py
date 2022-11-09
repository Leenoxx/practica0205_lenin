# Escribir un programa que pregunte por una muestra de números,
# separados por comas, los guarde en una lista y muestre por pantalla
# su media y desviación típica.

numeros = int(input("Escribe números (0 para finalizar): "))
lista = []

while numeros != 0:
    lista.append(numeros)
    numeros = int(input("Escribe números (0 para finalizar): "))

num = 0
cantidad = 0
for numero in lista:
    cantidad += 1
    num = num + numero
media = num / cantidad

print("La media de los números introducidos es ", media)

num_dos = 0
for i in lista:
    i = (i - media) ** 2
    num_dos = num_dos + i
num_dos = num_dos / cantidad

print("La desviación típica es", pow(num_dos, 0.5))
