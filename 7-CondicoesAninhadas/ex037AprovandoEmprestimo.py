casa = float(input('Valor da casa R$'))
salario = float(input('Salario do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
parcelaA = casa/anos
parcelaM = parcelaA/12
print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos a prestação sera de R${parcelaM:.2f} mensal')
if  (30/100)*salario > parcelaM:
    print('\033[1;32mEmprestimo Autorizado!\033[m')
else:
    print('\033[1;31mEmprestimo Negado!\033[m')
    