# ver se o número é PRIMO
num = int(input('digite um número inteiro: '))
tot = 0 #para saber o número de divisíveis
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m',end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[34mO número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('Por isso, ele é PRIMO!\n divide por 1 e por ele mesmo')
else:
    print('Por isso ele é não é primo')