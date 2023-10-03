
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
    
    
    
fechaActual = input("Ingrese la fecha actual en el siguiente formato (dia/mes/año)\n"
                    "-->")



print(fechaActual)
print(fechaNacimiento)