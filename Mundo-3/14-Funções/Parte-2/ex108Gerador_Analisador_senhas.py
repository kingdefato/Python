from random import choice
import string


def gerar_senhas(qtd, tamanho):
    lista = []
    todos = string.ascii_letters + string.digits + string.punctuation
    for _ in range(qtd):
        senha = ''.join(choice(todos) for _ in range(tamanho))
        lista.append(senha)
    return lista


def analisar_senhas(lista):
    maior = ''
    menor = lista[0]
    for s in lista:
        if len(s) < len(menor):
            menor = s
        if len(s) > len(maior):
            maior = s
    letras = numeros = simbolos = 0
    for senha in lista:
        for c in senha:
            if c in string.ascii_letters:
                letras += 1
            elif c in string.digits:
                numeros += 1
            elif c in string.punctuation:
                simbolos += 1

    return {
        'Maior Senha': maior,
        'Menor Senha': menor,
        'Média de Tamanho': sum(len(s) for s in lista) / len(lista),
        'Total de letras': letras,
        'Total de números': numeros,
        'Total de simbolos': simbolos
    }


senhas = gerar_senhas(5, 10)
resultado = analisar_senhas(senhas)
for s in senhas:
    print(f'Senha: {s}')

print('\n--- Análise ---')
for k, v in resultado.items():
    print(f'{k}: {v}')
