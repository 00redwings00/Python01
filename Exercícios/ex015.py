#escreva um progarama que pergunte a quantidade km percorridos por um carro alugado e quantidade de dias pelo qual ele foi alkugado.
km= int(input('Quantos km rodados: '))
d= int(input('Quantos dias de uso: '))
print('O valor a ser pago é de:R${:.2f}'.format((km*0.15)+(d*60)))