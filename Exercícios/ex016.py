#Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela sua porção inteira
#Ex: digite um numero: 6.127 --- O número 6.127 tem a parte inteira 6

from math import trunc
num = float(input('Digite um valor: '))
#print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))
real = trunc(num)
print('A porção inteira de {}, é {}'.format(num, real))
num = float(input('Digite um valor: '))

#print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))