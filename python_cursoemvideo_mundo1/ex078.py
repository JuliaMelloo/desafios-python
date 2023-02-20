valores = []
maiorvalor = 0
menorvalor = 0
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maiorvalor = menorvalor = valores[c]
    else:
        if valores[c] >= maiorvalor:
            maiorvalor = valores[c]
        if valores[c] <= menorvalor:
            menorvalor = valores[c]


print('*' * 50)
print(f'Os valores digitados foram {valores}')
print(f'O maior valor encontrado na lista é o {maiorvalor} na posição', end=' ')
for pos, v in enumerate(valores):
    if v == maiorvalor:
        print(f'{pos}...', end=' ')
print()
print(f'O menor valor encontrado na lista é o {menorvalor} na posição', end=' ')
for pos, v in enumerate(valores):
    if v == menorvalor:
        print(f'{pos}...', end=' ')
