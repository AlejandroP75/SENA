def leerNum(msg):
    while True:
        try:    
            iNum = int(input(msg))
            return iNum
        except ValueError:
            print("Ingrese un numero valido")

print("Bienvenido, programa que le calcula la tabla de multiplicar de forma decreciente")

n = leerNum("Ingrese el numero del cual quiere generar la tabla de multiplicar\n-->")

print(f"\nTABLA DE MULTIPLICAR DEL {n}")

for i in range(10, 0, -1):
    print(f"{n} x {i} = {n * i}")

print("\nGracias por usar nuestro programa")