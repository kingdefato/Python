def metade(num):
    return f'{num / 2:.2f}'


def dobro(num):
    return f'{num * 2:.2f}'


def aumentar(num, porcentagem):
    aumento = num + (num / porcentagem)
    return f'{aumento:.2f}'


def diminuir(num, porcentagem):
    reduzir = num - (num / porcentagem)
    return f'{reduzir:.2f}'