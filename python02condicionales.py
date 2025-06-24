print("Condicionales Python")
print("Introduzca un numero")
#numero es un string: "10"
# numero = input()
#numero es un int: 10
numero = int(input())
if (numero > 0):
    print(f"Numero {numero} positivo")
else:
    if (numero < 0):
        print(f"Número {numero} negativo")
    else:
        print(f"El número es cero")
print("Fin de programa")
