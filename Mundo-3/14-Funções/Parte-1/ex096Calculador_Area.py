def area(largura, comprimento):
    Area = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {Area}m².')


# Programa Principal
print('-'*30)
print('Controle de Terrenos')
print('-'*30)
largura = float(input('Largura (m):  '))
comprimento = float(input('Comprimento (m): '))
area(largura, comprimento)
