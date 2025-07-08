from datetime import datetime
def voto(nascimento):
    idade = datetime.now().year - nascimento
    print('-'*35)
    
    if idade < 16:
            return print(f'Com {idade} anos: VOTO NEGADO')
    elif idade >=16 and  idade <=18 or idade>65:
        return print(f'Com {idade} anos: VOTO OPCIONAL')
    else:
        return print(f'Com {idade} anos: VOTO OBRIGATÓRIO')



ano_nascimento = int(input('Ano de nascimento: '))
eleição = voto(ano_nascimento)
