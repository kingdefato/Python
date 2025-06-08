num = [3, 4, 8, 9]
num[0] = 22
num.append(3)
num.sort()
num.sort(reverse=True)
num.insert(3, 92)
num.pop(0)
if 4 in num:
    num.remove(4)
else:
    print(f'Não achei o número 4')
print(f'Essa lista tem {len(num)} elementos.')
for v in num:
    print(f'{v}...', end='')
valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')

print(f'Cheguei ao final da lista')
a = [2, 3, 4, 7]
b = a[:] # faz uma copia
b = a # faz uma ligação
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')