valor = float(input('Valor da casa: R$'))
sal = float(input('Salário do comprador: R$'))
tempo = int(input('Quantos anos de financeamento? '))
prestacao = valor / (tempo * 12)
mínimo  = (sal / 100) * 30
print(f'Para pagar uma casa de R${valor:.2f} em {tempo} anos a prestação será de R${prestacao:.2f}')

if prestacao <= mínimo:
    print('Seu emprestimo foi APROVADO!')
else:
    print('Seu emprestimo foi NEGADO.')
