#Vicente Yahir Lopez Vazquez - 240010
#determinar si es vocal abierta o cerrada

letra = (input("Ingresa una letra: "))



if letra == "a" or letra == "e" or letra == "o" or letra == "A" or letra == "E" or letra == "O":
    print ("la vocal que ingresaste es abierta")
elif letra == "i" or letra == "u" or letra == "I" or letra == "U":
    print ("la vocal que ingresaste es cerrada")
else:
    print ("no valido")