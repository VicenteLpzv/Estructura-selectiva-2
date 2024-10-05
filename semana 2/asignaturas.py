#Vicente Yahir Lopez Vazquez - 240010
#indicar si el estudiante es de la categoría veterano o regular
#e indicar el número de materias y los costos de la colegiatura.

datos = int(input("Ingresa cuanto paga por asignatura: "))
asig = int(input("Ingresa las asignaturas que lleva: "))

if datos == 30:
    cost = datos * asig
    print (f"Eres veterano y pagas {cost} pesos por tus {asig} asignaturas")
elif datos == 50:
    cost = datos * asig
    print (f"Eres regular y pagas {cost} pesos por tus {asig} asignaturas")
else:
    print ("Error, ingresaste un valor no válido")