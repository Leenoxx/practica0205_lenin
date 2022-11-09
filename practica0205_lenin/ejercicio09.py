# Escribir un programa que pida al usuario una palabra y muestre por
# pantalla el número de veces que contiene cada vocal.

palabra = input("Escribe una palabra: ")
lista = []

for letra in palabra:
    lista.append(letra)

a = lista.count("a")
e = lista.count("e")
i = lista.count("i")
o = lista.count("o")
u = lista.count("u")

print("La palabra", palabra, "contiene:\n",
      a, "veces la vocal a\n", e, "veces la vocal e\n",
      i, "veces la vocal i\n", o, "veces la vocal o\n",
      u, "veces la vocal u")
