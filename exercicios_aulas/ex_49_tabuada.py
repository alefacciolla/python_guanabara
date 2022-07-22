#TABUADA/calculadora
num = int(input('digite um número para ver sua tabuada: '))
print('=_='*12)
for c in range(0,11):
    print('{} x {:2} = {}'.format(num, c, num*c))