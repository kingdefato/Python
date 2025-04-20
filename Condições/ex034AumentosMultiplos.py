salario = float(input('Informe seu salario R$:'))
if salario>1250:
    print(f'Você tem direito a uma bonificação de 10%!\nSeu novo salario é R${salario*(10/100)+salario:.2f}')
if salario<=1250:
    print(f'Você tem direito a uma bonificação de 15%! \nSeu novo salario é R${salario*(15/100)+salario:.2f}')