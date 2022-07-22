# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raíz quadrada
#from re import T
#from this import d


n = float(input('digite um número: '))
d2 = n * 2
t = n*3
r = n ** (1/2)
# pode ser feita também com a função power, ou pow(num_base, expoente) - 
#                                o expoente para raiz quadrada é *(1/2)
#raiz quadrada pode ser representada por uma EXPONENCIAÇÃO
print('analisando o número {},\n o dobro é {},\n o triplo {},\n e a raíz quadrada {:.2f}.'.format(n,d2,t,r))