''' Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''
somapares = mai = scol = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range (0,3):
    for c in range (0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] %2 == 0: # A) A soma de todos os valores pares digitados.
            somapares += matriz[l][c]
print('=-'*30)      
for l in range (0, 3):
    for c in range (0, 3):
        print(f'[{matriz[l][c]:^5}]', end = '')
    print()
for l in range(0, 3): # B) A soma dos valores da terceira coluna.
    scol += matriz[l][2]
for c in range(0, 3): # C) O maior valor da segunda linha.
      if c == 0:
        mai = matriz[1][c]
      else:
          if matriz[1][c] > mai:
              mai = matriz[1][c]
print(f'A soma de todos os valores PARES digitados: {somapares}')
print(f'A soma dos valores da terceira COLUNA: {scol}')
print(f'O maior valor da segunda LINHA: {mai}')