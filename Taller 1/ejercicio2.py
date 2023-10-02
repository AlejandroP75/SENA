gradosFNewYork = 74

print("\nBienvenido\n"
      f"\nLa temperatura actual en New York en grados Fahrenheit es de: {gradosFNewYork}°F\n"
      "\n¿Desea conocer la temperatura en grados centígrados?")
while True:
    print("\nDigite 1 para si o 2 para no")
    opc = input("--> ")
    if (opc != "1") and (opc != "2"):
        print(opc)
        print("\nPor favor solo digita 1 o 2")
        continue
    elif opc == "1":
        gradosCNewYork = (gradosFNewYork - 32) * (5 / 9)
        print(f"\nLa temperatura actual en New York en grados centígrados es de: {gradosCNewYork:,.1f}°C\n") 
        break;
    else:
        break;
print("Gracias por usar nuestros servicios")