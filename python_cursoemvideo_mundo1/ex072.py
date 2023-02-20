n = ('zero', 'um', 'dois', 'três', 'quatro',
     'cinco', 'seis', 'sete', 'oito',
     'nove', 'dez', 'onze', 'doze',
     'treze', 'catorze', 'quinze',
     'dezesseis', 'dezessete', 'dezoito',
     'dezenove', 'vinte')
while True:
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        print('Tente novamente. ', end='')
    print(f'Você digitou o número {n[num]}')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if continuar == 'N':
        break
