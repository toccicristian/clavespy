
def lista_a_parrafo(lista=[]):
    cadena=''
    maxlen=0
    max([len(l) for l in lista])
    maxlen=max([len(l) for l in lista if len(l)])
    for l in lista:
        cadena+=f'{l.rstrip()}{(maxlen-len(l)+1)*" "}\n'
    return cadena


