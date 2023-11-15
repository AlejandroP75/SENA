print("Bienvenido, programa que muestra el producto de 1 hasta el numero ingresado\n")

n = int(input("Ingrese el numero N\n-->"))

num = 1
for i in range(1, n + 1):
    num *= i

print(f"\nEl producto de 1 hasta {n} es: {num}\n"
      "\nGracias por usar nuestro programa")

