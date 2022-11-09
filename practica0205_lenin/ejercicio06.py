# Escribir un programa que almacene las asignaturas de un curso
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
# en una lista, pregunte al usuario la nota que ha sacado en cada
# asignatura y elimine de la lista las asignaturas aprobadas.
# Al final el programa debe mostrar por pantalla las asignaturas
# que el usuario tiene que repetir.

lista = ["DAPI", "GPIT", "SIRC", "SIHD"]
notas = []
lista_suspenso = []
contador = 0

nota_dapi = int(input("Escribe la nota que has "
                      "sacado en DAPI: "))
notas.append(nota_dapi)
nota_gpit = int(input("Escribe la nota que has "
                      "sacado en GPIT: "))
notas.append(nota_gpit)
nota_sirc = int(input("Escribe la nota que has "
                      "sacado en SIRC: "))
notas.append(nota_sirc)
nota_sihd = int(input("Escribe la nota que has "
                      "sacado en SIHD: "))
notas.append(nota_sihd)

for nota in notas:
    if nota < 5:
        lista_suspenso.append(lista[contador])
        contador += 1
    else:
        contador += 1

print("")
for repetir in lista_suspenso:
    print("Debes repetir la materia de", repetir)
