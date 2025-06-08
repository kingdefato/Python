valores = []
maior = menor = 0
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {cont+1}: ')))
    if cont == 0:
        maior = menor = valores[cont]
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]
print(f'Você digitou os valores {valores}')
print(f'O maior valor foi: {maior}, nas posições', end=' ')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor foi: {menor}, nas posições', end=' ')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end='')
print()
