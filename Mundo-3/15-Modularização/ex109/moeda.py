def metade(num=0, moeda = False):
    if moeda:
        return formatar_moeda(num / 2)
    else:
        return num / 2


def dobro(num=0, moeda = False):
    if moeda:
        return formatar_moeda(num * 2)
    else:
        return num * 2


def aumentar(num=0, porcentagem=0, moeda = False):
    aumento = num + (num * porcentagem / 100)
    if moeda:
        return formatar_moeda(aumento)
    else:
        return aumento


def diminuir(num=0, porcentagem=0, moeda = False):
    reduzir = num - (num * porcentagem / 100)
    if moeda:
        return formatar_moeda(reduzir)
    else:
        return reduzir


def formatar_moeda(num=0, moeda='R$'):
    formatação = f'{moeda}{num:.2f}'.replace('.', ',')
    return formatação
