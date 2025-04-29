print('~='*20)
print('Analisador de Triângulos')
print('~='*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1< r2 + r3 and r2< r1 + r3 and r3< r1 + r2:
    print('É possivel formar um triângulo!')
    if r1 == r2 and r2 == r3:
        print('Sera formado um triângulo \033[4mEQUILÁTERO\033[m')
    elif r1 == r2 and r1 != r3 or r1 == r3 and r1 != r2:
        print('Sera formado um triângulo \033[4mISÓSCELES\033[m')
    else:
        print('Sera formado um triângulo \033[4mESCALENO\033[m')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo :/')