def leerInt(msg):
    while True:
        try:
            iNum = int(input(msg))
            return iNum
        except ValueError:
            print("Ingrese un numero entero valido")

print("Bienvenido, programa que permite ingresar 20 numeros y devulve los numeros menores o igual que 25\n\n")

numeros = []

cont = 0
while True:
    num = leerInt(f"Introduce el numero {cont + 1}\n-->")
    numeros.append(num)
    cont = cont + 1

    if cont > 3:
        break

for i in numeros:
    if i <= 25:
        print(i)

print("\nGracias por usar nuestro programa")