cont = soma = 0
num = int(input('Digite um valor: '))
while cont != num:
    if num < 0:
        break
    cont += 1
    if cont % 3 == 0 and cont % 5 == 0:
        print(f'{cont}->', end='')
        soma += cont
    else:
        if cont % 3 == 0:
            print(f'{cont}->', end='')
            soma += cont
        if cont % 5 == 0:
            print(f'{cont}->', end='')
            soma += cont
print(f'\nA soma dos números foi de {soma}')
