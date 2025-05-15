soma = contador = c = 0
while c != 999:
    c = int(input('Digite um valor [999 Para parar]: '))
    if c != 999:
        soma += c
        contador += 1
print(f'Foram {contador} valores digitados, e a soma deles é {soma}')