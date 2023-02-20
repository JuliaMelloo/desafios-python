# Tabela Brasileirão
lista = ('Flamengo', 'Palmeiras', 'Atlético Paranaense', 'Atlético Mineiro',
         'São Paulo', 'Fluminense', 'Fortaleza', 'Corinthians',
         'Santos', 'Internacional', 'Grêmio', 'América Mineiro',
         'Atlético Goianiense', 'Ceará',  'Bahia', 'Botafogo',
         'Red Bull Bragantino', 'Cruzeiro', 'Goiás', 'Cuiabá')
print('=-'*20)
print('Os 5 primeiros times são: ', end='')
for primeiros in lista[0:5]:  # Mostrará os primeiros 5 times
    print(f'{primeiros}, ', end='')
print('\n')
print('=-'*20)
print('Os últimos 4 colocados são: ', end='')
for últimos in lista[-4:]:   # Mostrará os últimos 4 times
    print(f'{últimos}, ', end='')
print('\n')
print('=-'*20)
print('Os times em ordem alfabética.')
alfa = (sorted(lista))
for c in alfa:
    print(f'{c}' , end=' ')
print('\n')
print('=-'*20)
print(f'''O time Ceará esta na posição {lista.index('Ceará')+1}º''')
print('=-'*20)
