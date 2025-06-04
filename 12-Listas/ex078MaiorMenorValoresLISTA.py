valores= list()
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {cont+1}: ')))
print('=-'*20)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {max(valores)} na posição {valores.index(max(valores))+1}...\nO Menor valor digitado foi {min(valores)} na posição {valores.index(min(valores))+1}...')
