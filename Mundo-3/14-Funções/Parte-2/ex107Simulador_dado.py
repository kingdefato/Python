from random import randint


def simular_dado(lados, rolagens):
    dado = dict()
    resultados = []
    for c in range(0, rolagens):
        resultados.append(randint(1, lados))
    frequência = {}
    for valor in resultados:
        if valor not in frequência:
            frequência[valor] = 1
        else:
            frequência[valor] += 1
    dado = {
        'Resultado': resultados,
        'Maior': max(resultados),
        'Menor': min(resultados),
        'Frequência': frequência
    }
    return dado


#Programa Principal
simulação = simular_dado(lados=8, rolagens=10)
for k, v in simulação.items():
    print(f'{k} = {v}')
print('\nFrequência de números:')
for valor, qtd in simulação['Frequência'].items():
    print(f'{valor} saiu {qtd}x')
