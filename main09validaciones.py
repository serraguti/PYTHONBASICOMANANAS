import library09validaciones as li
print("Ejemplo librerías")
print("Introduzca un email")
email = input()
respuesta = li.validarEmail(email)
print(f"El email {email} es {respuesta}")
print("Introduzca su numero de NIF")
numero = int(input())
letra = li.getLetraNif(numero)
print(f"La letra del NIF {numero} es {letra}")
print("Fin de programa")