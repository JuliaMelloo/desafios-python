sal = float(input('Qual é o salário atual do funcionario? R$ '))
if sal > 1250:
    atual = sal + (sal / 100 * 10)
    print(f'O salário do funcionario passará de R${sal:.2f} para R${atual:.2f}')
else:
    atual = sal + (sal / 100 * 15)
    print(f'O salário do funcionario passará de R${sal:.2f} para R${atual:.2f}')


