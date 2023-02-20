from random import randint
cont = 0
print('{:=^80}'.format(' VAMOS JOGAR PAR OU ÍMPAR '))
while True:
    num_jogador = int(input('Diga um valor entre 0 e 10: '))
    jogador = str(input('Par ou Ímpar [P/I]: ')).upper()
    num_computador = randint(0, 10)
    soma = num_jogador + num_computador
    divisao = soma % 2
    if divisao == 0:
        resul = 'PAR'
    else:
        resul = 'ÍMPAR'
    print('-' * 30)
    print(f'Você jogou {num_jogador} e o computador {num_computador}. Total de {soma} DEU {resul}!!')
    if jogador == 'P' and resul == 'PAR'  or jogador == 'I' and resul == 'ÍMPAR':
        cont += 1
        print('Você ganhou!!')
        print('-'*30)
    else:
        break
print(f'GAME OVER! Você venceu {cont} vezes')



