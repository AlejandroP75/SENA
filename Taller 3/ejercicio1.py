print("Bienvenido programa para calcular areas y perimetros ")
while True:
    print("\n-----MENU-----"
        "\n1.Triangulo"
        "\n2.Rectangulo"
        "\n3.Cuadrado"
        "\n4.Circulo")
    opc = int(input("\nIngrese el numero de la opción deseada\n--> "))
    if(opc < 1 or opc > 4):
        print("Por favor seleccione una opcion valida")
        continue
    break
if (opc == 1):
    while True:
        print("\nTRIANGULO")
        print("¿Que desea calcular?"
            "\n1.Perimetro"
            "\n2.Area")
        opt = int(input("\nIngrese el numero de la opción deseada\n--> "))
        if(opt < 1 or opt > 2):
            print("Por favor seleccione una opcion valida")
            continue
        break
    if (opt == 1):
        print("\nTRIANGULO - PERIMETRO")
        while True:
            at = float(input("Ingrese el valor del primer lado: "))
            if (at <= 0):
                print("\nEl valor no puede ser negativo o 0, vuelve a intentarlo\n")
                continue
            break
        while True:
            bt = float(input("Ingrese el valor del segundo lado: "))
            if (bt <= 0):
                print("\nEl valor no puede ser negativo o 0, vuelve a intentarlo\n")
                continue
            break
        while True:
            ct = float(input("Ingrese el valor del tercer lado: "))
            if (ct <= 0):
                print("\nEl valor no puede ser negativo o 0, vuelve a intentarlo\n")
                continue
            break
        perTri = at + bt + ct
        print(f"\nEl perimetro del triangulo es: {perTri:,.0f}")
    else:
        print("\nTRIANGULO - AREA")
        while True:
            baseT = float(input("Ingrese el valor de la base del triangulo: "))
            if (baseT <= 0):
                print("\nEl valor no puede ser negativo o 0, vuelve a intentarlo\n")
                continue
            break
        while True:
            altT = float(input("Ingrese el valor de la altura del triangulo respecto a la base y al pico superior: "))
            if (altT <= 0):
                print("\nEl valor no puede ser negativo o 0, vuelve a intentarlo\n")
                continue
            break
        areaTri = (baseT * altT)/2
        print(f"\nEl area del triangulo es: {areaTri:,.0f}")
elif (opc == 2):
    while True:
        print("\nRECTANGULO")
        print("¿Que desea calcular?"
            "\n1.Perimetro"
            "\n2.Area")
        opr = int(input("\nIngrese el numero de la opción deseada\n--> "))
        if(opr < 1 or opr > 2):
            print("Por favor seleccione una opcion valida")
            continue
        break
    if (opr == 1):
        print("\nRECTANGULO - PERIMETRO")
        while True:
            aR = float(input("Ingrese el valor de un lateral: "))
            if (aR <= 0):
                print("\nEl valor no puede ser negativo o 0, vuelve a intentarlo\n")
                continue
            break
        while True:
            bR = float(input("Ingrese el valor de la base: "))
            if (bR <= 0):
                print("\nEl valor no puede ser negativo o 0, vuelve a intentarlo\n")
                continue
            break
        perRec = 2 * (bR + aR)
        print(f"\nEl perimetro del rectangulo es: {perRec:,.0f}")
    else:
        print("\nRECTANGULO - AREA")
        while True:
            aR = float(input("Ingrese el valor de un lateral: "))
            if (aR <= 0):
                print("\nEl valor no puede ser negativo o 0, vuelve a intentarlo\n")
                continue
            break
        while True:
            bR = float(input("Ingrese el valor de la base: "))
            if (bR <= 0):
                print("\nEl valor no puede ser negativo o 0, vuelve a intentarlo\n")
                continue
            break
        areaRec = aR * bR
        print(f"\nEl area del rectangulo es: {areaRec:,.0f}")
elif (opc == 3):
    while True:
        print("\nCUADRADO")
        print("¿Que desea calcular?"
            "\n1.Perimetro"
            "\n2.Area")
        opcu = int(input("\nIngrese el numero de la opción deseada\n--> "))
        if(opcu < 1 or opcu > 2):
            print("Por favor seleccione una opcion valida")
            continue
        break
    if (opcu == 1):
        print("\nCUADRADO - PERIMETRO")
        while True:
            aC = float(input("Ingrese el valor de un lado: "))
            if (aC <= 0):
                print("\nEl valor no puede ser negativo o 0, vuelve a intentarlo\n")
                continue
            break
        perCua = 4 * aC
        print(f"\nEl perimetro del cuadrado es: {perCua:,.0f}")
    else:
        print("\nCUADRADO - AREA")
        while True:
            aC = float(input("Ingrese el valor de un lado: "))
            if (aC <= 0):
                print("\nEl valor no puede ser negativo o 0, vuelve a intentarlo\n")
                continue
            break
        areaCua = aC * aC
        print(f"\nEl area del cuadrado es: {areaCua:,.0f}")
else:
    while True:
        print("\nCIRCULO")
        print("¿Que desea calcular?"
            "\n1.Perimetro"
            "\n2.Area")
        opci = int(input("\nIngrese el numero de la opción deseada\n--> "))
        if(opci < 1 or opci > 2):
            print("Por favor seleccione una opcion valida")
            continue
        break
    if (opci == 1):
        print("\nCIRCULO - PERIMETRO")
        while True:
            rC = float(input("Ingrese el radio del circulo: "))
            if (rC <= 0):
                print("\nEl valor no puede ser negativo o 0, vuelve a intentarlo\n")
                continue
            break
        perCir = 2 * 3.141592 * rC
        print(f"\nEl perimetro del circulo es: {perCir:,.2f}")
    else:
        print("\nCIRCULO - AREA")
        while True:
            rC = float(input("Ingrese el radio del circulo: "))
            if (rC <= 0):
                print("\nEl valor no puede ser negativo o 0, vuelve a intentarlo\n")
                continue
            break
        areaCir = 3.141592 * (rC * rC)
        print(f"\nEl area del circulo es: {areaCir:,.2f}")
print("\nGracias por usar nuestro programa")