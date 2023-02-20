from time import sleep
print('{:=^81}'.format('\nCalculadora da Júlia Melo\n'))
opção = 0
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
while opção != 5:
    print('[ 1 ] SOMAR\n[ 2 ] MULTIPLICAR\n[ 3 ] MAIOR\n[ 4 ] NOVOS NÚMEROS\n[ 5 ] SAIR DO PROGRAMA')
    opção = int(input('Digite qual das opções acima deseja realizar? '))
    if opção == 1:
        print(f'A soma entre {n1} + {n2} é {n1 + n2}')
    elif opção == 2:
        print(f'O resultado da multiplicação de {n1} por {n2} é {n1 * n2}')
    elif opção == 3:
        if n1 > n2:
            print(f'O MAIOR valor digitado foi {n1}')
        elif n1 == n2:
            print(f'Os valores são iguais')
        else:
            print(f'O MAIOR valor digitado foi {n2} ')
    elif opção == 4:
        print('Informe os números novamente:')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
        opção == 5
        sleep(1)
    else:
        print('Opção inválida. Tente novamente')
    print('*'*20)
print('Fim do programa! Volte sempre!')
