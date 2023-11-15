def leerPrecio(msg):
    while True:
        try:    
            iNum = float(input(msg))
            if(iNum < 0):
                print("El precio no puede ser negativo")
                continue
            return iNum
        except ValueError:
            print("Ingrese un numero valido")

print("Bienvenido, programa en le que se suma el valor de 5 camisas en dolares y da el resultado en pesos colombianos\n\n")

c1 = leerPrecio("Ingrese el precio de la camisa 1 en dolares\n-->")
c2 = leerPrecio("Ingrese el precio de la camisa 2 en dolares\n-->")
c3 = leerPrecio("Ingrese el precio de la camisa 3 en dolares\n-->")
c4 = leerPrecio("Ingrese el precio de la camisa 4 en dolares\n-->")
c5 = leerPrecio("Ingrese el precio de la camisa 5 en dolares\n-->")

total = (c1 + c2 + c3 + c4 + c5) * 4027.61

print("\n\n-----FACTURA-----\n"
      f"\nCamiseta 1: ${c1:,.2f}"
      f"\nCamiseta 2: ${c2:,.2f}"
      f"\nCamiseta 3: ${c3:,.2f}"
      f"\nCamiseta 4: ${c4:,.2f}"
      f"\nCamiseta 5: ${c5:,.2f}"
      "\n----------------"
      f"\nTotal en dolares: ${c1+c2+c3+c4+c5:,.2f}"
      f"\nTotal en pesos colombianos: {total:,.0f} COP"
      "\n\nGracias por usar nuestro programa")