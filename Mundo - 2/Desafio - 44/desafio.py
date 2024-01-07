# IsacBM - 2K23
valor = float(input('Digite o preço do produto: '))
pag = str(input('Forma de pagamento: \n1- À vista (dinheiro/cheque) \n2- À vista no cartão \n3- 2x no Cartão \n4- 3 ou + vezes no cartão \nDigite: '))

dez = valor * 10/100
cinc = valor * 5/100
maisVezes = valor * 20/100

if pag == '1':
    print('O produto terá um desconto de 10%, sendo o novo valor R${}'.format(valor - dez))
elif pag == '2':
    print('O valor terá um desconto de 5%, sendo o novo valor R${}'.format(valor - cinc))
elif pag == '3':
    print('O valor não terá desconto, sendo o mesmo valor de R${}'.format(valor))
elif pag == '4':
    print('O valor sofrerá juros de 20%, sendo o preço final de R${}'.format(valor + maisVezes))
else:
    print('Escolha uma forma de pagamento...')
