from uteis import fatorial, dobro, triplo

# Programa Principal
num = int(input('Digite um valor: '))
fat = fatorial(num)
dob = dobro(num)
tri = triplo(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {dob}')
print(f'O triplo de {num} é {tri}')
