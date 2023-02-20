vel = float(input('Qual velocidade atual do carro? '))
multa = (vel - 80) * 7
if vel > 80:
    print('Você ultrapassou o limite de velocidade permitido cdfe 80km/h. MULTADO!')
    print(f'Valor da multa de R$ {multa}')
else:
    print('Você está dentro do limite de velocidade permitido!')
