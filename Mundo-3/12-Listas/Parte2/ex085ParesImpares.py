numeros = [[],[]]
for n in range(1, 8):
    n = int(input(f'Digite o {n}o valor: '))
    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)
numeros[0].sort()
numeros[1].sort()
print('-='*20)
print(f'Os valores pares são: {numeros[0]}')
print(f'Os valores ímpares são: {numeros[1]}') 