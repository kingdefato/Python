from datetime import datetime
def voto(nascimento):
    idade = datetime.now().year - nascimento
    print('-'*35)
    print(f'Com {idade} anos: ', end='')
    if idade < 16:
            return 'VOTO NEGADO'
    elif idade >=16 and  idade <=18 or idade>65:
        return 'VOTO OPCIONAL'
    else:
        return 'VOTO OBRIGATÓRIO'


ano_nascimento = int(input('Ano de nascimento: '))
eleição = voto(ano_nascimento)
print(eleição)