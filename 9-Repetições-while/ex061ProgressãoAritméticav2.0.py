print('='*40)
print(' '*10,'10 TERMOS DE UMA PA')
print('='*40)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo = primeiro
c = 1
while c <= 11:
    print(f'\033[1;35m{termo}\033[m', end=' → ')
    termo += razão
    c += 1
print('FIM')