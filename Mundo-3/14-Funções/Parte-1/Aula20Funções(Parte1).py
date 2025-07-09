from time import sleep
'''def soma(a, b):
    s = a + b
    print(f'A soma de {a} + {b} é igual a {s}')
    

soma(a=2, b=3)
soma(a=4, b=5)
soma(b=8, a=9)'''


'''def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.')

# Programa Principal
contador(2, 3, 4, 5)
contador(5, 6, 7, 8, 9)
contador(2, 3)'''


def dobra(lst):
    posição = 0
    while posição < len(lst):
        lst[posição] *= 2
        posição += 1


valores = [7, 3, 2, 6]
print(f'Valores: {valores}')
dobra(valores)
print(f'Dobrados: {valores}')
