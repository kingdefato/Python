sex = str(input('Qual seu sexo [M/F]: ')).upper().strip()[0] # [0] Pega apenas a primeira letra
while sex not in 'MF':
    sex = str(input('\033[1;31mDados invalidos.\033[m\nPor favor informe seu sexo: ')).upper().strip()[0]
print(f'Sexo \033[1;32m{sex}\033[m registrado com sucesso.')