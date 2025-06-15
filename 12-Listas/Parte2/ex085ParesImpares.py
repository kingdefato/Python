pares = []
ímpares = []
numeros = [[pares], [ímpares]]
for n in range(1, 8):
    n = int(input(f'Digite o {n}o valor: '))
    if n % 2 == 0:
        pares.append(n)
    else:
        ímpares.append(n)