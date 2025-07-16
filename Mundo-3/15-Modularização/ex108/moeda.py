def metade(num=0):
    return num / 2


def dobro(num=0):
    return num * 2


def aumentar(num=0, porcentagem=0):
    aumento = num + (num * porcentagem / 100)
    return aumento


def diminuir(num=0, porcentagem=0):
    reduzir = num - (num * porcentagem / 100)
    return reduzir


def moeda(num=0, moeda='R$'):
    formatação = f'{moeda}{num:.2f}'.replace('.', ',')
    return formatação
