peso = float(input('Qual seu peso? (Kg) '))
altura = float(input('Qual dua altura? (m)'))
imc = peso / (altura ** 2)
print(f'Seu IMC é de {imc:.1f}.')
if imc < 18.5:
    print('Você está ABAIXO DO PESO ideal.')
elif 18.5 <= imc < 25:
    print('PARABÉNS! Você está na faixa de PESO IDEAL!')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO.')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE.')
else:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')
