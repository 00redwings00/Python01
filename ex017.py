#faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa
import math
co= float(input('Digite o valor do cateto oposto: '))
ca= float(input('Digite o valor do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir: {:.2f}'.format(hi))

'''h= (co**2 + ca**2)**(1/2)
print('O valor da hipotenusa é: {:.2f}'.format(h))'''