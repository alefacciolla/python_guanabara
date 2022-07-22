#CALCULO DE PORCENTAGEM - ou calculando desconto
#Desafio 12 e 13 - preço e o novo preço
#Para calcular porcentagem,
# pode-se colocar o valor *x/100, sendo "x" a porcentagem
preço = float(input('qual o preço? '))
novo = preço - (preço * 0.15)
print('o produto que custa R${} com 15 de desconto fica R${:.2f}'.format(preço,novo))
# o simbolo de % é usado para o RESTO da divisão em python
#
# pode ser feita também com a função power, ou pow(num_base, expoente) - 
#                                o expoente para raiz quadrada é *(1/2)
#raiz quadrada pode ser representada por uma EXPONENCIAÇÃO
#print('analisando o número {},\n o dobro é {},\n o triplo {},\n e a raíz quadrada {:.2f}.'.format(n,d2,t,r))

# fórmula para converter celcius para farenheit 
# c = input numero e tal
# f = ((9*c)/5)+32