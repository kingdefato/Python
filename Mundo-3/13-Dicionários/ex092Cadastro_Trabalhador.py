'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente,
além da idade, com quantos anos a pessoa vai se aposentar.'''
from datetime import datetime
trabalhador = {}
trabalhador['Nome'] = input('Nome: ')
Nascimento = int(input('Data de nascimento: '))
trabalhador['Carteira de Trabalho'] =  int(input('Carteira de Trabalho (0 Não tem): '))
trabalhador['Idade'] = datetime.now().year - Nascimento
if trabalhador['Carteira de Trabalho'] != 0:
    trabalhador['Contratação'] = int(input('Ano de contratação: '))
    trabalhador['Salário'] = float(input('Salario: R$'))
    trabalhador['Aposentadoria'] = trabalhador['Idade'] + ((trabalhador['Contratação'] + 35) - datetime.now().year)
for k, v in trabalhador.items():
    print(f'    - {k} tem o valor de {v}')