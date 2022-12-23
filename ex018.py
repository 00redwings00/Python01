#faça um programa que leia um angulo qualquer e mostre na tela o valo do seno, cosseno e a tangente desse angulo
import math
n = float(input('Digite o valor de um ângulo: '))
sen = math.sin(math.radians(n))
cos = math.cos(math.radians(n))
tan = math.tan(math.radians(n))
print('O seno desse ângulo corresponde a: {:.2f} \nO cosseno desse ângulo corresponde a: {:.2f} \nE a tangente desse ângulo corresponde a: {:.2f}'.format(sen, cos, tan))
