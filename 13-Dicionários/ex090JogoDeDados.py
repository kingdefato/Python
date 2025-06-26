aluno = dict()
aluno['Nome'] = str(input('Nome: '))
aluno['Media'] = float(input('Media do Aluno: '))
if aluno['Media'] >= 7:
    aluno['Situação'] = '\033[32mAprovado\033[m'
else:
    aluno['Situação'] = '\033[31mReprovado\033[m'
for k, v in aluno.items():
    print(f'{k} é igual a {v}')