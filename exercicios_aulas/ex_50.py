# ler seis números inteiros e mostrar a
# soma dos que são PARES.
# se o valor digitado for impar, desconsidere
soma = 0
cont = 0
for c in range(1,7):
    num = int(input('digite o valor {}: '.format(c)))
    if num % 2 == 0:
        soma += num# quando envolve a mesma variável + outra, pode fazer assim
        cont += 1
print('Você informou {} números pares\n'
      'A soma de todos os pares é: {}'.format(cont, soma))