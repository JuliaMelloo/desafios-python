soma = 0
cont = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c} valor inteiro: '))
    if num % 2 == 0:
        soma += num
        cont += 1
if num % 2 == 0:
    print(f'Você digitol {cont} números pares e a soma foi de {soma}')
else:
    print('ERRO, você digitou somente números impares, tente novamente')