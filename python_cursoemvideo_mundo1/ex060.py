n = int(input('Digite um número para ver seu fatorial: '))
print(f'Calculando o fatorial de {n}! = ', end='')
cont = n
resul = 1
while cont > 0:
    print(f'{cont}', end='')
    print(' x ' if cont > 1 else ' = ', end='')
    resul *= cont
    cont -= 1
print(resul)
