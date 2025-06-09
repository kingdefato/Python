lista = []
maior = menor = 0
for c in range(1,5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]: #se o n for maior do que o ultimo elemento da lista
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista): # vai fazer uma varredura da posição zero até a ultima posição de lista
            if n <= lista[pos]: # se o número for menor ou igual a ele , vai incerir o valor em uma posição especifica
                lista.insert(pos, n) # insere o valor na poisção pos
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-='*30)
print(f'Os valores digitados em ordem foram {lista}')
                