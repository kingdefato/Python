largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))
area = largura*altura
tintanecessária = area/2
print(f'Uma parede com a largura de {largura} e uma altura de {altura} metros com uma área de {area}m², sera necessário {tintanecessária:.2f}L de tinta para pintar a parede')