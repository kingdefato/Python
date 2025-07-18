def leiaDinheiro(msg):
    ok = False
    while not ok:
        entrada = str(input(msg)).replace(',','.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[31mERRO! {entrada} é um preço inválido.\033[m')
        else:
            valor = float(entrada)
            ok = True
    return valor