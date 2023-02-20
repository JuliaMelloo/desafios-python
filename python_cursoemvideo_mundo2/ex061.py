print('{:=^100}'.format(' \n10 TERMOS DE UMA PA\n'))
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 1
termo = primeiro
while cont < 10:
    print(termo, end=' ')
    cont += 1
    termo += razao
print('Acabou')
