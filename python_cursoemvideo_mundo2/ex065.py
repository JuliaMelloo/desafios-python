n = int(input('Digite um número: '))
maior = menor = soma = n
media = 0
r = False
cont = 1
while r != True:
    n = int(input('Digite um número: '))
    cont += 1
    soma += n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    r = str(input('Deseja para [S/N]? ')).upper()
    if r == 'S':
        r = True
    elif r == 'N':
        r = False
    else:
        print('Dados inválidos. Tente novamente.')
media = (soma / cont)
print(f'''O maior número digitado foi {maior}
O menor valor digitado {menor}
E a média entre os {cont} valores digitados foi de {media}''')
