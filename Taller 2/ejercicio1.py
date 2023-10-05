while True:
    fechaNacimiento = input("Ingrese la fecha de su nacimiento en el siguiente formato (dia/mes/año)\n"
                        "--> ")
    fNlist = fechaNacimiento.split("/")
    if (int(fNlist[2]) < 1) or (int(fNlist[2]) > 2023):
        print("El año tiene que estar entre 1 y 2023, vuelve a intentarlo")
        continue
    elif (int(fNlist[1]) < 1) or (int(fNlist[1]) > 12):
        print("El mes tiene que estar entre 1 y 12, vuelve a intentarlo")
        continue
    
    bisiesto = False
    if ((int(fNlist[2]) % 4) == 0):
        bisiesto = True
        if((int(fNlist[2]) % 100) == 0):
            if((int(fNlist[2]) % 400) != 0):
                bisiesto = False
    if (int(fNlist[1]) == 1) or (int(fNlist[1]) == 3) or (int(fNlist[1]) == 5) or (int(fNlist[1]) == 7) or (int(fNlist[1]) == 8) or (int(fNlist[1]) == 10) or (int(fNlist[1]) == 12):
        if(int(fNlist[0]) < 0) or (int(fNlist[0]) > 31):
            print("El numero de días es mayor al posible de ese mes, vuelve a intentarlo")
            continue
    if (int(fNlist[1]) == 4) or (int(fNlist[1]) == 6) or (int(fNlist[1]) == 9) or (int(fNlist[1]) == 11):
        if(int(fNlist[0]) < 0) or (int(fNlist[0]) > 30):
            print("El numero de días es mayor al posible de ese mes, vuelve a intentarlo")
            continue
    if (int(fNlist[1]) == 2):
        if(bisiesto == True):
            if(int(fNlist[0]) < 0) or (int(fNlist[0]) > 29):
                print("El numero de días es mayor al posible de ese mes, vuelve a intentarlo")
                continue    
        else:
            if(int(fNlist[0]) < 0) or (int(fNlist[0]) > 28):
                print("El numero de días es mayor al posible de ese mes, vuelve a intentarlo")
                continue  



while True:
    fechaActual = input("Ingrese la fecha actual en el siguiente formato (dia/mes/año)\n"
                        "-->")
    fAlist = fechaActual.split("/")



print(fechaActual)
print(fechaNacimiento)