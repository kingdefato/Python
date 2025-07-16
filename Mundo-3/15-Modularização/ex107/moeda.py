def metade(num):
    return f'{num / 2:.2f}'


def dobro(num):
    return f'{num * 2:.2f}'


def aumentar(num, porcentagem):
    aumento = num + (num * porcentagem / 100)
    return f'{aumento:.2f}'


def diminuir(num, porcentagem):
    reduzir = num - (num * porcentagem / 100)
    return f'{reduzir:.2f}'
