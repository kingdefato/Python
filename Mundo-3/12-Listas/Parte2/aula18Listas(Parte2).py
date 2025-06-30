'''teste = list()
teste.append('Ytallo')
teste.append(16)
galera = list()
galera.append(teste[:])
teste[0] = 'Junior'
teste[1] = 12
galera.append(teste[:])
print(galera)'''
grupo = [['Ytallo', 16],['Bryan', 16],['Pedro aga', 17],['Carol', 16]]
print(grupo[0][1], grupo[2][1])
for pessoa in grupo:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.')
maior = menor = 0
dado = list()
galera = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print('-='*20)
print(galera)
for p in galera:
    if p[1] >=21:
        print(f'{p[0]} É maior de idade')
        maior += 1
    else:
        print(f'{p[0]} É menor de idade')
        menor += 1
print(f'{maior} são maiores, {menor} são menores')