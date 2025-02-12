
def SNo(n):
    return n + 1

def ANo(n):
    if n > 0:
        return n - 1
    else:
        raise ValueError("Tiene que ser un numero mayor que 0.")

def suma(a, b):
    if b == 0:
        return a
    else:
        return suma(SNo(a), ANo(b))
        
def multiplicacion(a, b):
    if b == 0:
        return 0
    else:
        return suma(a, multiplicacion(a, ANo(b)))
        
def resta(a, b):
    if b == 0:
        return a
    else:
        return resta(ANo(a), ANo(b))

def division(a, b):
    if b == 0:
        raise ValueError("Math Error, no se puede dividir por 0.")
    if a < b:
        return 0
    else:
        return SNo(division(resta(a, b), b))
