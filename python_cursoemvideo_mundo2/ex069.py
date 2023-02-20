maior_dezoito = mulher_menorvinte = homem = 0
while True:
    print('{:-^99}'.format('\nCADASTRE UMA PESSOA\n'))
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [F/M]: ')).strip().upper()[0]
    print('-'*50)
    stop = ' '
    while stop not in 'SN':
        stop = str(input('Deseja continuar? [S/N]? ')).strip().upper()[0]
    if idade >= 18:
        maior_dezoito += 1
    if idade < 20 and sexo == 'F':
        mulher_menorvinte += 1
    if sexo == 'M':
        homem += 1
    if stop == 'N':
        break
print(f'''No grupo {maior_dezoito} pessoas tem mais de 18 anos
{homem} homens ao todo no grupo e {mulher_menorvinte} mulheres menores de vinte anos!''')

