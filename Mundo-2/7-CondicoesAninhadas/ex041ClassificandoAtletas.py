from datetime import date
anoatual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = anoatual-nascimento
print(f'O Atleta tem \033[1m{idade}\033[m Anos')
if    idade <=9:
    print('Classificação: \033[4mMIRIM\033[m')
elif  idade <=14:
    print('Classificação: \033[4mINFANTIL\033[m')
elif  idade <=19:
    print('Classificação: \033[4mJÚNIOR\033[m')
elif  idade <=25:
    print('Classificação: \033[4mSÊNIOR\033[m')
else:
    print('Classificação: \033[4mMASTER\033[m')