soma = 0 #acumulador
cont = 0 #contador
for num in range(1, 501, 2):
    if num%3 == 0:
        cont += 1
        soma += num
print(f'A soma de todos os {cont} valores solicitados é {soma}')
