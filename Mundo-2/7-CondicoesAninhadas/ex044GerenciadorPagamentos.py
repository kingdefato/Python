print( f'{'Loja':=^40}')
preço = float(input('Preço da compra R$:'))
print('''   \033[4mFORMAS DE PAGAMENTO\033[m
[1] À vista DINHEIRO/CHEQUE
[2] À vista CARTÃO
[3] 2x no CARTÃO
[4] 3x ou mais no CARTÃO''')
opção = int(input('Opção de pagamento: '))
if opção == 1:
    total = preço - (preço * 10/100)
    print('Você tem direito a 10% de desconto!')
    print(f'Valor total a pagar R$:\033[1m{total:.2f}\033[m')
elif opção == 2:
    total = preço - (preço * 5/100)
    print('Você tem direito a 5% de desconto!')
    print(f'Valor total a pagar R$:\033[1m{total:.2f}\033[m')
elif opção == 3:
    print(f'Valor total a pagar: 2x de R$:{preço/2:.2f} SEM JUROS')
elif opção == 4:
    parcelas = int(input('Em quantas vezes deseja parcelar: '))
    print('Minimo de 3 parcelas.')
    total = preço + (preço * 20/100)
    totalparcelas = total / parcelas
    print(f'Valor total a pagar: {parcelas}x de R$:{totalparcelas:.2f} COM JUROS')
    print(f'A sua compra de R${preço:.2f} vai custar R${total:.2f} ao total.')
else:
    print('\033[1;31mOpção invalida! Tente Novamente.\033[m')