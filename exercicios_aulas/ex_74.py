# programa p/
# 1 - gerar 5 números aleatórios em uma tupla.
# 2 - mostrar a listagem de números gerados e
# 3 - indicar o menor e maior valor dentro da tupla gerada
from random import randint
numeros = (randint(1,10), randint(1,10), randint(1,10),randint(1,10),randint(1,10))
print(f'Os valores sorteados foram: ', end=' ')
for n in numeros:
    print(f'{n}', end=' ')
print(f'\nO MAIOR valor sorteado foi: {max(numeros)}')
print('-_='*9)
print(f'O MENOR valor foi {min(numeros)}')

