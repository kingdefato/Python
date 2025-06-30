
num = (int(input('Digite um numero: ')),int(input('Digite um numero: ')),int(input('Digite um numero: ')),int(input('Digite um numero: ')))
print(f'Os números digitados foram {num}')
print(f'O número 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O numero 3 apareceu na {num.index(3)+1}ª posição')
else:
    print('O número 3 não foi digitado')
print('Os valores pares digitados foram: ', end=' ')
for n in num:   
    if n % 2 == 0:
        print(n, end=' ')
