salario = float(input('Informe seu salario R$:'))
if salario>1250:
    print(f'Você tem direito a uma bonificação de 10%!\nSeu salario de \033[1;31mR${salario:.2f}\033[m foi para \033[1;32mR${salario*(10/100)+salario:.2f}\033[m')
if salario<=1250:
    print(f'Você tem direito a uma bonificação de 15%! \nSeu salario de \033[1;31mR${salario:.2f}\033[m foi para \033[1;32mR${salario*(15/100)+salario:.2f}\033[m')