def validarEmail(email):
    if (email.find("@") == -1):
        return False
    elif (email.count(".") == 0):
        return False
    elif (email.startswith("@") == True or email.endswith("@") == True):
        return False
    elif (email.count("@") > 1):
        return False
    elif (email.find("@") > email.rfind(".")):
        return False
    else:
        #posicion del ultimo punto
        ultimoPunto = email.rfind(".")
        dominio = email[ultimoPunto + 1:]
        if (len(dominio) >= 2 and len(dominio) <= 3):
            return True
        else:
            return False

def getLetraNif(numeroDni):
    resultado = numeroDni % 23
    letrasDni="TRWAGMYFPDXBNJZSQVHLCKET"
    letra = letrasDni[resultado]
    return letra