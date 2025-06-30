while True:
    n = int(input('Digite o numero que você deseja saber a tabuada [Valor negativo para parar]: '))
    print('=-'*20)
    if n <0:
        break
    for c in range (1,11):
        print(f'{n} x {c} = {n*c}')
    print('=-'*20)
print('Programa Encerrado. Volte Sempre!')