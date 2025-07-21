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
                f'\033[31mERRO! Houve um problema com os tipos de dados informados. {error.__class__} (USE APENAS NUMEROS INTEIROS)\033[m')
        if ok:
            break
    return valor


def leiaFloat(msg):
    valor = 0
    while True:
        n = str(input(msg)).replace(',', '.')
        try:
            valor = float(n)
        except KeyboardInterrupt:
            print('\033[31mO Usuário preferiu não digitar esse numero.\033[m')
            return 0 
        except (ValueError, TypeError):
            print(
                f'\033[31mERRO! Houve um problema com os tipo de dados informados. (USE APENAS NUMEROS Reais) \033[m')
            continue  # joga pro while novamente para tentar mais uma vez
        else:
             return valor


    # Programa Principal
n = leiaInt('Digite um numero inteiro: ')
n2 = leiaFloat('Digite um numero Real: ')
print(f'Voce digitou o numero {n}, e {n2}')
