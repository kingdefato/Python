tempo = int(input('Quantos anos tem seu carro: '))
if tempo <=3:
    print('Carro novo!')
else:
    print('Carro velho 😢')
print('--FIM--')
# print('carro novo'if tempo <=3 else 'carro velho')
nome = str(input('Qual é o seu nome?'))
if nome == 'Ytallo':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print(f'Bom dia {nome}!')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1+n2) /2
print(f'A sua media foi {media:.1f}')
if media >=6.0:
    print('Sua média foi boa!')
else:
    print('Sua média foi ruim!')