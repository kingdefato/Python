a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
#Maior
if a > b and a > c:
    print(f'O maior valor é {a}')
if b > a and b > c :
    print(f'O maior valor é {b}')
if c > a and c > b:
    print(f'O maior valor é {c}')
#Menor
if a < b and a < c:
    print(f'O menor valor é {a}')
if b < a and b < c:
    print(f'O menor valor é {b}')
if c < a and c < b:
    print(f'O menor valor é {c}')
