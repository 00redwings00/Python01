#faça um algoritmo que leia o slario de um funcionario e mostre seu novo salario com 15% de aumento
n= float(input('Digite o valor do seu salário atual: '))
print('Hoje você está recebendo um aumento permamente \n E seu salário passa a ser: R${:.2f} reais'. format(n+(n*0.15)))
