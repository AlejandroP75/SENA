def leerFloat(msg):
    while True:
        try:    
            iNum = float(input(msg))
            return iNum
        except ValueError:
            print("Ingrese un numero racional valido")

print("Bienvenido, programa que segun el capital y el intereses le informa cuando se duplica")
while True:
    cap = leerFloat("Ingrese el valor del capital\n--> ")
    if(cap < 0):
        print("El numero del capital no puede ser negativo, vuelva a intentarlo")
        continue
    break

while True:
    interes = leerFloat("Ingrese el valor del interes anual\n--> ")
    if(interes < 0):
        print("El numero del interes no puede ser negativo, vuelva a intentarlo")
        continue
    break

interes = interes / 100
tiempo = 0
capIt = cap

while (capIt < 2 * cap):
    capIt *= (1 + interes)
    tiempo += 1

print(f"Segun el interes el valor se duplicara en {tiempo} años"
      "Gracias por usar nuestro programa")