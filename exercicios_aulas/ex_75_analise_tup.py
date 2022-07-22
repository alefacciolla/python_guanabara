#Programa que leia 4 valores e guardeos em uma tupla
num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais número: ')),
       int(input('Digite um último número: ')))
print(f'Você digitou os valores {num}')
#Ao final, mostre
# a) quantas * valor 9
print(f'O valor 9 apareceu {num.count(9)} vezes')
# b) posição no index do primeiro valor 3
if 3 in num:
    print(f'o valor 3 apareceu na {num.index(3) + 1}ª posição ')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
# c) quais são os números pares
print('os valores PARES digitados foram: ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')