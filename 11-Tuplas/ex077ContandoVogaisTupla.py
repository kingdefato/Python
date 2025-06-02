palavras = ('Bola', 'Macaco', 'Queijo', 'Pastor', 'Amor', 'Peixe', 'Teclado', 'Caneta', 'Celular', 'Monitor')
for n in palavras:
    print(f'\nNa Palavra \033[4m{n.upper()}\033[m temos: ',end='')
    for letra in n:
        if letra.lower() in 'aeiou':
            print(letra.upper(), end=' ')
    