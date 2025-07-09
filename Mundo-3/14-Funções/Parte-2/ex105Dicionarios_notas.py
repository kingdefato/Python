def notas(*n, sit=False):
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
