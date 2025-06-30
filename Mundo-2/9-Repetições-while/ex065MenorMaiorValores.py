num = media = quant = maior = menor = soma = 0
s = 'S'
while s in 'Ss':
        num = int(input('Digite um valor: '))
        quant += 1
        soma += num
        if quant == 1 :
            maior = menor = num
        else:
            if num > maior:
                maior = num
            if num < menor:
                menor = num
        s = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
media = soma / quant       
print(f'Você digitou {quant} números e a média desses valores é {media:.2f}')
print(f'O Maior valor foi {maior} e o Menor foi {menor}')