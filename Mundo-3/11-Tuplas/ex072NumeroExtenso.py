núm = 'zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
ler = int(input('Digite um número de 0 a 20: '))
while ler >20 or ler<0 :
    ler = int(input('Tente Novamente. Digite um número de 0 a 20: '))
print(f'Você digitou o número: {núm[ler].capitalize()}')