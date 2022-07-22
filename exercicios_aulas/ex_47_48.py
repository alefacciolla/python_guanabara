# Desafio 47
for n in range(2, 51, 2):# pulando de 2 em 2
    #if n % 2 == 0: #se for par
    print(n,end=' ')
print('Acabou')

# Desafio 48
#some todos os números primos de 0 a 500
soma = 0 # ACUMULADOR
cont = 0 # CONTADOR
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1 # contador soma UM
        soma = soma + c # acumulador soma um valor
        #print(c, end=' ')
print('-='* 20)
print('A SOMA de todos os {} números ímpares múltiplos de 3\n'
      'no intervalo entre 1 e 500 é: {}'.format(cont, soma))