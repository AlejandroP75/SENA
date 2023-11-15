entrevistados = []
registrados = 0

while True:
    print("\nBienvenido, software de la emisora ACME")
    while True:
        print("\n-----MENU-----\n"
            "\n1.Agregar persona"
            "\n2.Mostrar la información de una persona")
        opc = int(input("\nSeleccione una opción\n-->"))
        if (opc < 1 or opc > 2):
            print("\nOpción no valida, vuelva a intentarlo")
            continue
        break

    if (opc == 1):
        print("\n-----AGREGAR PERSONA-----")
        print(f"\nNumero de personas registradas: {registrados}")
        if (registrados == 6):
            print("No se pueden agregar mas personas")
            continue
        persona = []
        artistas = []
        canciones = []

        nom = input("Ingrese el nombre: ")
        doc = int(input("Ingrese el documento: "))
        fechaNac = input("Ingrese la fecha de nacimiento en el sigueinte formato (dd/mm/aa): ")
        correo = input("Ingrese el correo electronico: ")
        ciudadRes = input("Ingrese la ciudad de residencia: ")
        ciudadOrg = input("Ingrese la ciudad de origen: ")

        print("Canciones favoritas")
        cont = 0
        while True:
            cancion = input("Ingrese el nombre de la canción: ")
            artista = input("Ingrese el nombre del artista: ")
            canciones.append(cancion)
            artistas.append(artista)
            cont = cont + 1
            if (cont == 3):
                break
            while True:
                opa = int(input("Si desea agregar a otra cancion con su artista digite 1, si no quiere digite 2: "))
                if(opa < 1 or opa > 2):
                    print("Seleccione una opción valida")
                    continue
                break
            if (opa == 1):
                continue
            break
        
        persona.append(nom)
        persona.append(doc)
        persona.append(fechaNac)
        persona.append(correo)
        persona.append(ciudadRes)
        persona.append(ciudadOrg)
        persona.append(canciones)
        persona.append(artistas)

        entrevistados.append(persona)

        registrados = registrados + 1
        print("\nPERSONA AGREGADA\n")
        input("Presione enter para volver al menu principal")
        continue

    else: 
        while True:
            print("\nINFORMACIÓN PERSONA")
            print(f"\nNúmero de personas registradas: {registrados}")
            ide = int(input("Ingrese la posición del vector de la persona de la que quiere conocer la información: "))

            if ide < 0 or ide >= registrados:
                print("Posición del vector no encontrada")
                continue
            else:
                print(f"\nNombre: {entrevistados[ide][0]}"
                      f"\nDocumento: {entrevistados[ide][1]}"
                      f"\nFecha de nacimiento: {entrevistados[ide][2]}"
                      f"\nCorreo: {entrevistados[ide][3]}"
                      f"\nCiudad de residencia: {entrevistados[ide][4]}"
                      f"\nCiudad de origen: {entrevistados[ide][5]}"
                      f"\nCanciones: {entrevistados[ide][6]}"
                      f"\nArtista: {entrevistados[ide][7]}")
                break
        break
print("\nGracias por usar nuestro programa")


