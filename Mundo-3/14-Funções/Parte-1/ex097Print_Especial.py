def escreva(txt):
    tam = len(txt) + 4
    print('-' * tam)
    print(f'  {txt}')
    print('-' * tam)


# Programa Principal
txt = str(input('Digite algo: '))
escreva(txt)