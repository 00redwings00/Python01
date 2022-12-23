#calcule a sua area e quantidade de tinta necessaria para pinta-lo, sabendo que cada litro de tinta pinta uma area de 2m2
largura= float(input('Digite a largura da sua parede: '))
altura= float(input('Digite a altura da sua parede: '))
area= largura*altura
tinta= 2.0
print('Você precisa de {:.2f} litros de tinta para pintar sua parede'.format(area/tinta))
