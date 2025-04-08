d = int(input('Quantidade de dias pelos quais ele foi alugado: '))
km = float(input('Quantos km foram percorridos: '))
print(f'O valor total a ser pago é R${km * 0.15 + d * 60:.2f}')