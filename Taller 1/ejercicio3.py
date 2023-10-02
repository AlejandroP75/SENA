def validar():
    
    while True:
        num = int(input("--> "))
        if (num < 0):
            print("ERROR: Los minutos no pueden ser negativos, vuelva a intentarlo")
            continue
        return num
            


print("\nBienvenido, vamos a crear un plan detallado personalizado para ti\n")
while True:
    llegada = input("¿A que horas tienes que llegar al trabajo? Ingresa la información en el siguiente formato (Hora:Minutos)\n"
                    "La hora debe estar en formato de 24horas\n"
                    "--> ")
    horaLlegada = llegada.split(":")
    if ((int(horaLlegada[0]) < 1) or (int(horaLlegada[0]) > 23)) or ((int(horaLlegada[1]) < 0) or (int(horaLlegada[1]) > 59)):
        print("\nA introducido mal la hora, vuelva a intentarlo\n")
        continue
    break
print("¿Cuanto demoras de tu casa al trabajo? (en minutos)")
transporte = validar()
print("¿Cuanto demoras en alistarte? (en minutos)")
alistarse = validar()
print("¿Cuanto demoras en hacer y comer tu desayuno? (en minutos)")
desayuno = validar()

horaLevantarseHor = int(horaLlegada[0])
horaLevantarseMin = int(horaLlegada[1]) - transporte - alistarse - desayuno

while(horaLevantarseMin < 0):
    horaLevantarseMin = horaLevantarseMin + 60
    horaLevantarseHor = horaLevantarseHor - 1

print("\nPlan detallado\n"
      f"\nLevantarse: {horaLevantarseHor}:{horaLevantarseMin}"
      "\nDesayunar: "
      "\nAlistarte: "
      "\nSalir de casa al trabajo: ")