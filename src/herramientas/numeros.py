def es_numero(n):
    try:
        float(n)
        return True
    except ValueError:
        return False


def modulo(n):
    if n<0:
        return n*-1
    return n


def rota_b(val_b=0,veces=0,reverso=False, bits=256):
    if not reverso:
        r=val_b+veces
        if r > bits:
            r=r-bits
        return r
    r=val_b-veces
    if r < 0:
        r=bits+r
    return r

