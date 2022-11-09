# Escribir un programa que almacene el abecedario en una lista,
# elimine de la lista las letras que ocupen posiciones múltiplos de 3,
# y muestre por pantalla la lista resultante.

abecedario = ["a", "b", "c", "d", "e", "f", "g",
              "h", "i", "j", "k", "l", "m", "n",
              "ñ", "o", "p", "q", "r", "s", "t",
              "u", "v", "w", "x", "y", "z"]
contador = 27
for i in abecedario[::-1]:
    if contador % 3 == 0:
        abecedario.remove(i)
        contador -= 1
    else:
        contador -= 1

print(abecedario)
