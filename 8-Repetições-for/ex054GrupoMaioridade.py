from datetime import date
maior = 0
menor = 0
ano = date.today().year
for c in range(1,8):
    nascimento = int(input(f'Ano em que a {c}º nasceu? '))
    idade = ano - nascimento
    if idade >=18:
        maior += 1
    else:
        menor += 1
print(f'Ao todo {maior} pessoas ja atingiram a maior idade.')
print(f'E também tivemos {menor} pessoas que ainda não antigiram a maior idade.')