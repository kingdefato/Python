def leiaDinheiro(msg):
    ok = False
    while not ok:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[31mERRO! {entrada} é um preço inválido.\033[m')
        else:
            valor = float(entrada)
            ok = True
    return valor


def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[31mERRO! Digite um número válido.\033[m')
        if ok:
            break
    return valor
