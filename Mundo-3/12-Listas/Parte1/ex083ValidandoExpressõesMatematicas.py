expr = str(input('Expressão: '))
pilha = list()
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else: # teve mais parenteses fechando do que abrindo
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Expressão válida!')
else:
    print('Expressão invalida')