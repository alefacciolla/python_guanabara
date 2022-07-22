import math
#Podemos importar só a sub biblioteca, como
# from math import sqrt, floor, etc
#                  - desta forma não precisa usar o math antes
num = int(input('digite um numero: '))
raiz = math.sqrt(num)

print('a raiz de {} é igual a {:.2f}'.format(num,raiz))
#
