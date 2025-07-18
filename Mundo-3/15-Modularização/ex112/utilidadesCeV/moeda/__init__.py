def metade(num=0, moeda=False):
    if moeda:
        return formatar_moeda(num / 2)
    else:
        return num / 2


def dobro(num=0, moeda=False):
    if moeda:
        return formatar_moeda(num * 2)
    else:
        return num * 2


def aumentar(num=0, porcentagem=0, moeda=False):
    aumento = num + (num * porcentagem / 100)
    if moeda:
        return formatar_moeda(aumento)
    else:
        return aumento


def diminuir(num=0, porcentagem=0, moeda=False):
    reduzir = num - (num * porcentagem / 100)
    if moeda:
        return formatar_moeda(reduzir)
    else:
        return reduzir


def formatar_moeda(num=0, moeda='R$'):
    formatação = f'{moeda}{num:.2f}'.replace('.', ',')
    return formatação


def resumo(num=0, aumento=0, reduzir=0):

    print('-'*40)
    print(f'{'RESUMO DO VALOR':^40}')
    print('-'*40)

    print(f'Preço Analisado:{formatar_moeda(num): >24}')
    print(f'Dobro do Preço: {dobro(num, True): >24}')
    print(f'Metade do Preço:{metade(num, True): >24}')
    print(f'{aumento}% de Aumento:{aumentar(num, aumento, True): >25}')
    print(f'{reduzir}% de redução:{diminuir(num, reduzir, True): >25}')

    print('-'*40)
