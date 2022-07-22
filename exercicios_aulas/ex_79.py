# 79 - vários valores numéricos e coloca numa lista.
# a) Caso o número já exista, não será adicionado
# b) Ao final, todos os valores únicos em ordem crescente
numeros = list()
while True:
    n = int(input('digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado!')
    else:
        print('Valor duplicado! Portanto, não adicionado')
    r = str(input('quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('-='*30)
numeros.sort()
print(f'Voce digitou os valores {numeros}')

