# Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.

palabra = input("Escribe una palabra: ")
lista = []

for letra in palabra:
    lista.append(letra)

lista_dos = list(lista)
lista_dos.reverse()

if lista == lista_dos:
    print("La palabra", palabra, "SÍ es un palíndromo")
else:
    print("La palabra", palabra, "NO es un palíndromo")