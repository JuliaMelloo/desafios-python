frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for c in range(len(junto) -1, -1, -1):
    inverso += junto[c]
print(f'O inverso de {junto} é {inverso}')
if c == frase:
    print('Temos um palíndromo!')
else:
    print('A frase não é palíndromo!')

""" OU """

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print(f'O inverso de {junto} é {inverso}')
if c == frase:
    print('Temos um palíndromo!')
else:
    print('A frase não é palíndromo!')
