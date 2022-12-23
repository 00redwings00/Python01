#faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
n= float(input('Digite aqui o preço do seu produto: '))
print('O preço do seu produto com 5% de desconto é: {:.2f}'.format(n-(n*0.05)))