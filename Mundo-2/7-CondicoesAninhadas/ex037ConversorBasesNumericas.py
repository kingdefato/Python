num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] Converter para \033[1;32mBINÁRIO\033[m
[ 2 ] Converter para \033[1;32mOCTAL\033[m
[ 3 ] Converter para \033[1;32mHEXADECIMAL\033[m''')
opção = int(input('Sua opção: '))
if opção == 1:
    print(f'O número {num} convertido para \033[1;32mBINÁRIO\033[m é igual a \033[4;36m{bin(num)[2:]}\033[m')
elif opção == 2:
    print(f'O número {num} convertido para \033[1;32mOCTAL\033[m é igual a \033[4;36m{oct(num)[2:]}\033[m')
elif opção == 3:
    print(f'O número {num} convertido para \033[1;32mHEXADECIMAL\033[m é igual a \033[4;36m{hex(num)[2:]}\033[m')
else:
    print('\033[1;31mOpção inválida! Tente Novamente.\033[m')