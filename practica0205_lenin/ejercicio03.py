# Escribir un programa que almacene las asignaturas de un curso
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
# en una lista, pregunte al usuario la nota que ha sacado en cada
# asignatura, y después las muestre por pantalla con el mensaje
# En <asignatura> has sacado <nota> donde <asignatura> es cada
# una des las asignaturas de la lista y <nota> cada una de las
# correspondientes notas introducidas por el usuario.

lista = ["DAPI", "GPIT", "SIRC", "SIHD"]
notas = []
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

print("")
for asignatura in lista:
    print("En", asignatura, "has sacado", notas[contador])
    contador = contador + 1
