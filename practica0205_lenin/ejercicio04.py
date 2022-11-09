# Escribir un programa que pregunte al usuario los números ganadores
# de la lotería primitiva, los almacene en una lista y los muestre
# por pantalla ordenados de menor a mayor.

lista = []
num_premiado = int(input("Introduce los números ganadores"
                         "(0 para finlizar): "))
while num_premiado != 0:
    lista.append(num_premiado)
    num_premiado = int(input("Introduce los números ganadores"
                             "(0 para finlizar): "))
lista.sort()

for i in lista:
    print(i)
