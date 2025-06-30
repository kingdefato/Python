print('='*40)
print(' '*10,'10 TERMOS DE UMA PA')
print('='*40)
termo = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
decimo = termo + (11-1) * razão
for c in range(termo, decimo, razão):
    print(f'\033[1;35m{c}\033[m', end=' → ')
print('Acabou.')