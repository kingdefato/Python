import math
ctoposto = float(input('Comprimento do cateto oposto: '))
ctadjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = ctoposto**2 + ctadjacente**2
resultado = math.sqrt(hipotenusa)
print(f'O valor da hipotenusa é {resultado:.2f}')
# hipotenusa = math.hypot(ctoposto, ctadjancente)