def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        try:
            valor = int(n)
            ok = True
        except Exception as error:
            print(
                f'\033[31mERRO! Digite um numero válido. \033[m')
        if ok:
            break
    return valor


def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRICIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[35mSua Opção: \033[m')
    return opc