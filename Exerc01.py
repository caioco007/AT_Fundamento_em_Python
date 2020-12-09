tupla = (8,11,10)

def crescente(tupla):
    lista = list(tupla)
    lista.sort()
    return tuple(lista)

print(crescente(tupla))