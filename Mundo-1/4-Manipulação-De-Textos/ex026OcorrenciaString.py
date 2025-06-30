frase = str(input('Escreva uma frase: ')).lower().strip()
print('A letra A aparace' ,frase.count('a'), 'vezes')
print(f'Aparece pela primeira vez na posição {frase.find('a')+1}')
print(f'Aparece pela ultima vez na posição {frase.rfind('a')+1}')