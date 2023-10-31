edades = []
menores = 0
mayores = 0
adultoMayor = 0
promedio = 0

print("Bienvenido, programa para dar información sobre 10 edades suministradas por el usuario")

i = 0
while True:
    while True:
        edad = int(input(f"\nIngrese la edad {i+1}: "))
        if (edad < 1 or edad > 120):
            print("\nEdad no valida, vuelva a intentarlo")
            continue
        break
    edades.append(edad);
    i = i + 1
    if (i == 10):
        break

for x in edades:
    if (x < 18):
        menores = menores + 1
    elif (x >= 18 and x < 60):
        mayores = mayores + 1
    else:
        adultoMayor = adultoMayor + 1

    promedio = promedio + x
    

print("\n-----INFORME DE EDADES-----"
      f"\n\nMenores de edad: {menores}"
      f"\nMayores de edad: {mayores}"
      f"\nAdultos mayores de edad: {adultoMayor}"
      f"\nMenor edad ingresada: {min(edades)}"
      f"\nMayor edad ingresada: {max(edades)}"
      f"\nEdad promedio: {promedio/10}")
print("\nGracias por usar nuestro programa")