nome = str(input('Escreva seu nome completo:')).strip()
print(nome.upper())
print(nome.lower())
nome = nome.split()
a = ''.join(nome)
print('O primeiro nome tem o total de',len(a),'letras')
# print(f'O primeiro nome tem o total de{len(nome)- nome.count(' ')}')  outra forma de contar o numero total de letras
print('O primeiro nome tem', len(nome[0]),'letras')
# print(f'O primeiro nome tem {nome.find(' ')}')  outra forma de contar as letras do primeiro nome