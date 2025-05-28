print('-'*40)
print(f'{'SEQUENCIA DE FIBONACCI': ^40}')
print('-'*40)
termos = int(input('Quantos termos você quer mostrar? '))
c = 1
t1 = 0
t2 = 1
print('~'*40)
print(f'{t1} → {t2}', end='')
while c <= termos:
    t3 = t1 + t2
    print(f' → {t3}', end='')
    t1 = t2
    t2 = t3
    c+= 1
print(' → FIM')
print('~'*40)