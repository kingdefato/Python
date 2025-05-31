lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita'
# print(lanche[1:3])
for cont in range (0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for comida in lanche:
    print(f'Eu vou comer {comida}')

for pos , comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print(sorted(lanche)) # Mostra em ordem
print(lanche)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(len(c))
print(c.count(5)) # Quantas vezes aparece o número 5 na variavel C
print(c.index(8)) # Em que posição esta o número 8

pessoa = ('Ytallo', 16, 'M', 66.8)
# del(pessoa)
print(pessoa)