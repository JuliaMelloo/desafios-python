print('{:=^100}'.format(' \n10 TERMOS DE UMA PA\n'))
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 1
termo = primeiro
ate = 11
while cont <= ate:
    print(termo, end=' ')
    cont += 1
    termo += razao
    for c in range(cont == ate):
        mais = int(input('\nQuantos termos você quer mostrar a mais? '))
        ate += mais
print(f'Progressão finalizada com {cont} termos mostrados')
