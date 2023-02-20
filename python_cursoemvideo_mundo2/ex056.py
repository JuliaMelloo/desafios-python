soma_idade = 0
menor_vinte = 0
maior_idade = 0
nomemaior = ''
for c in range(1, 5):
    print('{:-^30}'.format(f' {c}º PESSOA '))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().lower()
    soma_idade += idade
    if c == 1 and sexo == 'm':
        maior_idade = idade
        nomemaior = nome
    if idade > maior_idade and sexo == 'm':
        maior_idade = idade
        nomemaior = nome
    if idade < 20 and sexo == 'f':
        menor_vinte += 1
media = soma_idade / 4
print(f'''A média de idade do grupo foi de {media}.
{nomemaior} é o homem mais velho do grupo com {maior_idade} anos.
No grupo tem {menor_vinte} mulheres com menos de 20 anos.''')
