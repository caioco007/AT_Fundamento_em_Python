base=int(input("Digite o valor da base: "))
expoente=int(input("Digite o valor do expoente: "))

def potencia (base, expoente):
    potencia=1

    for x in range(expoente):
        print(x)
        potencia *= base

    print(base,"^",expoente,"=",potencia)

potencia(base,expoente)

