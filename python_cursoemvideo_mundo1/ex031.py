distancia = float(input('Qual a distancia da sua viajem em Km? '))
print(f'Você está prestes a começar uma viajem de {distancia} Km.')
if distancia <= 200:
    preço = 0.50 * distancia
else:
    preço = 0.45 * distancia
print(f'Sua passagem vai custar R${preço:.2f}')
