print('\033[1:33m*-' * 20)
print('\033[1:32mALISTAMENTO MILITAR')
print('\033[1:33m*-\033[m' * 20)

sexo = int(input('Qual seu sexo? '
                 '[1] FEMININO '
                 '[2] MASCULINO   '))
if sexo == 1:
    print('Você não tem obrigatoriedade em se alistar!')
else:
    from datetime import date

    atual = date.today().year
    nasc = int(input('Ano de nascimento: '))
    idade = atual - nasc
    alistamento = nasc + 18
    print(f'Quem nasceu no ano de {nasc} tem {idade} anos de idade no ano de {atual}.')
    if idade < 18:
        print('Ainda faltam {} anos para o alistamento.'.format(18 - idade))
        print(f'Seu alistamento será em {alistamento}')
    elif idade == 18:
        print('Deve se alistar IMEDIATAMENTE!')
    else:
        print('Você já deveria ter se alistado a {} anos.'.format(atual - alistamento))
        print(f'Seu alistamento foi em {alistamento}.')
