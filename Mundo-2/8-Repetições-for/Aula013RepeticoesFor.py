for c in range(1, 10, 3):
   print(c)
print('fim')

n = int(input('Digite um numero: '))
for c in range (n, 0,-1):
   print(c)

i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range (i, f+1, p):
   print(c)

for c in range(0,3):
    n = int(input('Dgite um valor: '))
print('Fim')

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print(f'O somatorio de todos os valores foi {s}')