def leerFloat(msg):
    while True:
        try:    
            iNum = float(input(msg))
            return iNum
        except ValueError:
            print("Ingrese un numero racional valido")

print("Bienvenido, programa para convertir de grados Centígrados a grados Fahrenheit\n")


gradosC = leerFloat("Ingrese el numero de grados Centígrados\n--> ")
gradosF = (9 / 5) * gradosC + 32

print(f"\nGrados Centígrados = {gradosC:,.0f}\n"
      f"Grados Fahrenheit = {gradosF:,.0f}\n"
      "\nGracias por usar nuestro programa")