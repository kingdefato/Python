n1 = float(input('Nota do primeiro bimestre: '))
n2 = float(input('Nota do segundo bimestre: '))
media = (n1+n2) / 2
print(f'Tirando a media de {n1:.2f} e {n2:.2f} a sua nota é: {media:.1f}')
if media < 5:
    print('\033[1;31mNota insuficiente, REPROVADO!\033[m')
elif media >= 5 and media <=6.9:
    print('\033[1;33mNota insuficiente, RECUPERAÇÃO!\033[m')
elif media >6.9:
    print('\033[1;32mNota Suficiente, APROVADO!\033[m')