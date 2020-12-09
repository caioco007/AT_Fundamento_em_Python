num=int(input("Some os números pares do 1 até:"))
lista = []
for x in range(1,num):
    if x % 2 == 0:
        lista.append(x)
soma = sum(lista)
print("Valor: ",soma)
