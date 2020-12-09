tupla = (1,8,5,8,2,7,6,9,8,9)

def pares(tupla):
    par = [n for n in tupla if n % 2 == 0]
    return tuple(par)
print(pares(tupla))

def impares(tupla):
    impar = [n for n in tupla if n % 2 != 0]
    return impar
print(impares(tupla))