print("Validacion de email")
email = input("Introduzca email: ")
# •	Que el email contenga una @
# •	Que el email contenga un punto
# •	@ ni al inicio ni al final
# •	Solamente una @ en el mail
# •	Un punto después de la @
# •	Dominio de 2 a 3 caracteres
if (email.find("@") == -1):
    print("No existe @")
elif (email.count(".") == 0):
    print("No existe punto")
elif (email.startswith("@") == True or email.endswith("@") == True):
    print("@ al inicio o al final")
elif (email.count("@") > 1):
    print("Solamente una @ en el mail")
elif (email.find("@") > email.rfind(".")):
    print("Debe existir un punto despues de la @")
else:
    #posicion del ultimo punto
    ultimoPunto = email.rfind(".")
    #Recuperamos el dominio a partir de la posicion
    #del ultimo punto
    dominio = email[ultimoPunto + 1:]
    if (len(dominio) >= 2 and len(dominio) <= 3):
        print("Email correcto")
    else:
        print("El dominio debe ser de 2 a 3 caracteres")
print("Fin de programa")
