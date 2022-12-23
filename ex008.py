#escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros
n= float(input('Digite o valor em metros, a ser convertido: '))
print('Esse valor corresponde a: {:.0f}cm \n E também corresponde a: {:.0f}mm'.format(n*100, n*1000))

