from random import randint
from time import sleep
item = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opções
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual sua jogada? '))
print('JO')
sleep(1)
print('KEM')
sleep(1)
print('PO!!!')
print('-=' * 11)
print(f'Você escolheu {item[jogador]}')
print(f'O computador escolheu {item[computador]}')

if jogador == 0 and computador == 2 or jogador == 1 and computador == 0 or jogador == 2 and computador == 1:
    print('Você GANHOU!!')
elif computador == 0 and jogador == 2 or computador == 1 and jogador == 0 or computador == 2 and jogador == 1:
    print('Computador GANHOU!!')
elif computador == jogador:
    print('Houve um EMPATE!!')
else:
    print('Erro. Tente novamente!')
