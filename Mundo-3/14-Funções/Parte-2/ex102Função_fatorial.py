def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número.
    :param num: O número a ser calculado o fatorial.
    :param show: (opcional) Se True, mostra o cálculo do fatorial.
    :return: O valor do fatorial de um número.
    Se show for True, imprime o cálculo passo a passo.
    Se show for False, retorna apenas o valor do fatorial.
    """
    f = 1
    if show == False:
        for c in range(num, 0 , -1):
            f*= c
        return f
    if show == True:
        for c in range (num, 0, -1):
            f*= c
            print(f'{c}', end='')
            print(' x ' if c>1 else ' = ', end='')
        return f
   
        
#Programa Principal
print(fatorial(5, True))
print(fatorial(5))
help(fatorial)
# A função fatorial recebe dois parâmetros: num e show.