vec1 = [0]
vec2 = [0]

print("\n-----PRIMER VECTOR-----")
cont = 0
while True:
    while True:
        dat = int(input("\nIngrese una dato para el vector (positivo)\n--> "))
        if dat < vec1[-1]:
            print("\nSe deben ingresar de forma ascendente, vuelva a intentarlo")
            continue
        break
    if (vec1[0] == 0):
        vec1.remove(0)
    print("\nDATO GUARDADO\n")
    vec1.append(dat)

    cont = cont + 1
    if (cont == 5):
        break

    while True:
        opc = int(input("¿Desea ingresar otro dato? (1 para sí, 2 para no)\n--> "))
        if (opc < 1 or opc > 2):
            print("\nIngrese una opción valida")
            continue
        break
    if (opc == 2):
        break

print("\n-----SEGUNDO VECTOR-----")
cont = 0
while True:
    while True:
        dat = int(input("\nIngrese una dato para el vector (positivo)\n--> "))
        if dat < vec2[-1]:
            print("\nSe deben ingresar de forma ascendente, vuelva a intentarlo")
            continue
        break
    if (vec2[0] == 0):
        vec2.remove(0)
    print("\nDATO GUARDADO\n")
    vec2.append(dat)

    cont = cont + 1
    if (cont == 5):
        break

    while True:
        opc = int(input("¿Desea ingresar otro dato? (1 para sí, 2 para no)\n--> "))
        if (opc < 1 or opc > 2):
            print("\nIngrese una opción valida")
            continue
        break
    if (opc == 2):
        break

for x in vec2:
    vec1.append(x)
    
vec1.sort()

print(f"\nEl vector resultante es {vec1}")
print("\nGracias por usar nuestro programa")
