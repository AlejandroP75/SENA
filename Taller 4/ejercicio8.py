def leerNum(msg):
    while True:
        try:    
            iNum = int(input(msg))
            if(iNum < 0 or iNum > 59):
                print("El numero no puede ser negativo o mayor que 59")
                continue
            return iNum
        except ValueError:
            print("Ingrese un numero valido")

def leerNum2(msg):
    while True:
        try:    
            iNum = int(input(msg))
            if(iNum < 0 or iNum > 23):
                print("El numero no puede ser negativo o mayor que 23")
                continue
            return iNum
        except ValueError:
            print("Ingrese un numero valido")

print("Bienvenido, programa que le calcula la hora en el segundo siguiente")

hora = leerNum2("Ingrese el numero de horas\n--> ")
minuto = leerNum("Ingrese el numero de minutos\n--> ")
segundo = leerNum("Ingrese el numero de segundos\n--> ")

print(f"\nHora ingresada = {hora}:{minuto}:{segundo}")

segundo = segundo + 1

if (segundo == 60):
    segundo = 0
    minuto = minuto + 1

if (minuto == 60):
    minuto = 0
    hora = hora + 1

if (hora == 24):
    segundo = 0
    minuto = 0
    hora = 0

print(f"\nHora ingresada mas un segundo = {hora}:{minuto}:{segundo}"
      "Gracias por usar nuestro programa")

