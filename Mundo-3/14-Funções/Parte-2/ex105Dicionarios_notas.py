def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação dos alunos
    """
    aluno = dict()
    aluno['Total de Notas'] = len(n)
    aluno['Nota Maxima'] = max(n)
    aluno['Nota Mínima'] = min(n)
    aluno['Media'] = sum(n) / len(n)
    if sit:
        if aluno['Media'] < 5:
            aluno['Situação'] = 'RUIM'
        elif 5 <= aluno['Media'] <= 7.5:
            aluno['Situação'] = 'RAZOÁVEL'
        else:
            aluno['Situação'] = 'BOM'
    return aluno


# Programa Principal
c = 1
nota = []
while True:
    n = float(input(f'Nota {c}º: '))
    nota.append(n)
    go = ' '
    while go not in 'SN':
        go = input('Quer continuar? [S/N]: ').strip().upper()
    c += 1
    if 'N' in go:
        break

resp = notas(*nota, sit=True)
print(resp)
help(notas)
