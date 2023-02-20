print('{:=^40}'.format(' LOJAS MELLO '))
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[1] á vista dinheiro/pix
[2] á vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
pagamento = int(input('Qual é a opção? '))

if pagamento == 1:
      print('Suas compras ficaram com desconto á vista de R${} para R${}'.format(preço, preço / 100 * 90))
elif pagamento == 2:
      print('Suas compras tiveram desconto no cartão á vista de R${} para R${}'.format(preço, preço / 100 * 95))
elif pagamento == 3:
      print('Total das suas compras ficaram R${} em duas vezes de R${} no cartão'.format(preço, preço / 2))
elif pagamento == 4:
      juros = preço + (preço / 100 * 20)
      parc = float(input('Quantas parcelas? '))
      print('Sua compra será parcelada em {}x de R${} COM JUROS'.format(parc, juros / parc))
      print(f'A compra de R${preço} vai custar R${juros} no final.')
else:
      print('Erro, tente novamente!')
