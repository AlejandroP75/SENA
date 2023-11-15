def leerConsumo(msg):
    while True:
        try:    
            iNum = float(input(msg))
            if(iNum < 0):
                print("El consumo no puede ser negativo")
                continue
            return iNum
        except ValueError:
            print("Ingrese un numero valido")

print("Bienvenido, programa que aplica el descuento si el consumo es mayor a 5000")

clientes = []
cont = 1

while True:
    numCli = int(input("Ingrese el numero de clientes\n-->"))
    if (numCli < 1):
        print("El numero de clientes no puede ser negativo o 0, vuelva a intentarlo")
        continue
    break

while True:
    num = leerConsumo(f"Ingrese el consumo del cliente {cont}\n-->")
    clientes.append(num)

    cont = cont + 1

    if(cont > numCli):
        break

cont2 = 1
for i in clientes:
    if(i > 5000):
        des = i * 0.2
        i = i - des
    print(f"\nSaldo a cancelar cliente {cont2}: {i:,.0f}")
    cont2 = cont2 + 1

print("Gracias por usar nuestro programa")