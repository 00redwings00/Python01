#crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
#considere US$1,00 = R$3,27
n= float(input('Digite o valor que você tem na carteira:R$ '))
print('Você pode comprar US${:.2f} dólares, com esse valor!'.format(n/3.27))
