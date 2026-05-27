def RaizQuad(a):
    resp = -1

    if(isinstance(a, int) and a > 0):
        resp = a ** 0.5
    
    return resp


def Potencia(a, b):
    resp = -1

    if(isinstance(a, int) and isinstance(b, int)):
        resp = a ** b

    return resp