def busca_argumento(argumentos=[], argumento='',separador='='):
  for arg in argumentos:
    if arg.startswith(argumento+separador):
      return (arg.split(separador)[1].rstrip() or ('',))
  return False


def existe_al_menos_uno(argumentos=[],buscar_en_lista=[],separador='='):
  for argumento in argumentos:
    for entrada in buscar_en_lista:
      if entrada.split(separador)[0] == argumento or entrada.rstrip() == argumento:
        return True
  return False


def existe_argumento(argumentos=[],argumento='',separador='='):
  for argum in argumentos:
    if argum.split(separador)[0] == argumento:
      return True
  return False
