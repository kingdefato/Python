peso = float(input('Seu peso (kg): '))
altura = float(input('Sua Altura (cm): '))
imc = peso / ((altura/100)**2)
print(f'O IMC é de \033[4m{imc:.1f}\033[m.')
if imc <= 18.5:
    print('Você esta Abaixo do Peso!')
elif imc <=25:
    print('Você esta no Peso Ideal!')
elif imc <=30:
    print('Você esta com Sobrepeso!')
elif imc <=40:
    print('Você esta com Obesidade!')
else:
    print('Você esta com Obesidade Mórbida')
