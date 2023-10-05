import math

while True:
    fechaNacimiento = input("Ingrese la fecha de su nacimiento en el siguiente formato (dia/mes/año)\n"
                        "--> ")
    fNlist = fechaNacimiento.split("/")
    diaN = int(fNlist[0])
    mesN = int(fNlist[1])
    añoN = int(fNlist[2])
    if (añoN < 1) or (añoN > 2023):
        print("El año tiene que estar entre 1 y 2023, vuelve a intentarlo")
        continue
    elif (mesN < 1) or (mesN > 12):
        print("El mes tiene que estar entre 1 y 12, vuelve a intentarlo")
        continue
    bisiesto = False
    if ((añoN % 4) == 0):
        bisiesto = True
        if((añoN % 100) == 0):
            if((añoN % 400) != 0):
                bisiesto = False
    if (mesN == 1) or (mesN == 3) or (mesN == 5) or (mesN == 7) or (mesN == 8) or (mesN == 10) or (mesN == 12):
        if(diaN < 0) or (diaN > 31):
            print("El numero de días es mayor al posible de ese mes, vuelve a intentarlo")
            continue
    if (mesN == 4) or (mesN == 6) or (mesN == 9) or (mesN == 11):
        if(diaN < 0) or (diaN > 30):
            print("El numero de días es mayor al posible de ese mes, vuelve a intentarlo")
            continue
    if (mesN == 2):
        if(bisiesto == True):
            if(diaN < 0) or (diaN > 29):
                print("El numero de días es mayor al posible de ese mes, vuelve a intentarlo")
                continue    
        else:
            if(diaN < 0) or (diaN > 28):
                print("El numero de días es mayor al posible de ese mes, vuelve a intentarlo")
                continue
    break  

while True:
    fechaActual = input("Ingrese la fecha actual en el siguiente formato (dia/mes/año)\n"
                        "-->")
    fAlist = fechaActual.split("/")
    diaA = int(fAlist[0])
    mesA = int(fAlist[1])
    añoA = int(fAlist[2])
    if (añoA < 1) or (añoA > 2023):
        print("El año tiene que estar entre 1 y 2023, vuelve a intentarlo")
        continue
    elif (mesA < 1) or (mesA > 12):
        print("El mes tiene que estar entre 1 y 12, vuelve a intentarlo")
        continue
    bisiesto = False
    if ((añoA % 4) == 0):
        bisiesto = True
        if((añoA % 100) == 0):
            if((añoA % 400) != 0):
                bisiesto = False
    if (mesA == 1) or (mesA == 3) or (mesA == 5) or (mesA == 7) or (mesA == 8) or (mesA == 10) or (mesA == 12):
        if(diaA < 0) or (diaA > 31):
            print("El numero de días es mayor al posible de ese mes, vuelve a intentarlo")
            continue
    if (mesA == 4) or (mesA == 6) or (mesA == 9) or (mesA == 11):
        if(diaA < 0) or (diaA > 30):
            print("El numero de días es mayor al posible de ese mes, vuelve a intentarlo")
            continue
    if (mesA == 2):
        if(bisiesto == True):
            if(diaA < 0) or (diaA > 29):
                print("El numero de días es mayor al posible de ese mes, vuelve a intentarlo")
                continue    
        else:
            if(diaA < 0) or (diaA > 28):
                print("El numero de días es mayor al posible de ese mes, vuelve a intentarlo")
                continue
    totalN = diaA + (mesA * 30) + (añoA * 365)
    totalA = diaA + (mesA * 30) + (añoA * 365)
    if (totalA < totalN):
        print("La fecha de nacimiento no puede ser mayor a la fecha actual, vuelve a intentarlo")
        continue
    break

edad = math.floor((totalA-totalN)/365)
print(f"Usted tiene : {edad} años"
      "Gracias por usar nuestro programa")
