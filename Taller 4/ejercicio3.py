def leerNota(msg):
    while True:
        try:    
            iNum = float(input(msg))
            if(iNum < 0 or iNum > 5):
                print("El valor de la nota debe estar entre 0.0 y 5.0, vuelva a intentarlo")
                continue
            return iNum
        except ValueError:
            print("Ingrese un numero entero valido")


print("Bienvenido, programa para saber cuanto se saco en el primer parcial de análisis\n")

t1 = leerNota("Ingrese la nota de 0 a 5 del primer taller\n--> ")
t2 = leerNota("Ingrese la nota de 0 a 5 del segundo taller\n--> ")
q1 = leerNota("Ingrese la nota de 0 a 5 del quiz\n--> ")
p1 = leerNota("Ingrese la nota de 0 a 5 del parcial\n--> ")

notaParcial = ((t1 + t2 + q1) / 3) * 0.3 + p1 * 0.7

print(f"\nTaller 1 = {t1}\n"
      f"Taller 2 = {t2}\n"
      f"Quiz = {q1}\n"
      f"Parcial = {p1}\n"
      "--------------------\n"
      f"Nota Final = {notaParcial:,.2f}\n\n"
      "Gracias por usar nuestro programa")