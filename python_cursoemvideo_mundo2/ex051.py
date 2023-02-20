print('{:=^100}'.format(' \n10 TERMOS DE UMA PA\n'))
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + 1, razao):
    print(c, end='.. ')
print('Acabou')
