def leerInt(msg):
    while True:
        try:
            iNum = int(input(msg))
            return iNum
        except ValueError:
            print("Ingrese un numero entero valido")

print("Bienvenido, programa para calcular el tiempo medio por kilometro recorrido\n")

while True:
    horas = leerInt("Ingrese el numero de horas que se demoro en el maratón\n--> ")
    if (horas < 0):
        print("El numero de horas no puede ser negativo, vuelva a intentarlo")
        continue
    break

while True:
    minutos = leerInt("Ingrese el numero de minutos que se demoro en el maratón\n--> ")
    if ((minutos < 0) or (minutos >= 60)):
        print("El numero de minutos no puede ser negativo o mayor e igual a 60, vuelva a intentarlo")
        continue
    break

totMinutos = (horas * 60) + minutos
minKm = totMinutos / 42.195;

print(f"\nTiempo= {horas}:{minutos}\n"
      f"Tiempo medio por kilometro= {minKm:,.2f} minutos\n\n"
      "Gracias por usar nuestro programa")