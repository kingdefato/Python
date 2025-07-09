def voto(nascimento):
    from datetime import date
    idade = date.today().year - nascimento
    print('-'*35)
    print(f'Com {idade} anos: ', end='')
    if idade < 16:
        return 'VOTO NEGADO'
    elif 16 <= idade < 18 or idade > 65:
        return 'VOTO OPCIONAL'
    else:
        return 'VOTO OBRIGATÓRIO'


# Programa principal
ano_nascimento = int(input('Ano de nascimento: '))
print(voto(ano_nascimento))
