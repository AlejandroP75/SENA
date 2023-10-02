#Se desea elaborar un algoritmo que permita identificar la cantidad de dólares equivalentes a una cantidad de pesos colombianos. 
dolar1 = 4144.2

print("\nBienvenido a nuestra casa de cambio\n")
while True:
    pesosColombianos = input("Ingrese el numero de pesos colombianos que desea convertir a dolares --> ")
    if pesosColombianos == "":
        print("Por favor ingrese un numero")
        continue;
    dolares = (float(pesosColombianos)/dolar1)
    print(f"\nPesos colombianos: ${float(pesosColombianos):,.0f}\n"
          f"Dolares: ${dolares:,.2f}")
    break;
print("\nGracias por usar nuestros servicios")