print('='*40)
print(' '*10,'10 TERMOS DE UMA PA')
print('='*40)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo = primeiro
c = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while c != total:
        print(f'{termo}', end=' → ')
        termo+=razão
        c += 1
    print(' \033[1mPAUSA\033[m')
    mais = int(input('Quantos valores a mais deseja mostrar? '))
print(f'Progressão finalizada, com {total} Termos exibidos.')