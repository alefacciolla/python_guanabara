# FAÇA uma função chamada maior() que receba n parametros inteiros
# tem que analisar todos os valores e dizer qual o maior
from time import sleep
def maior(*num):# com o asterisco, diz que tem vários parametros
    cont = maior = 0
    print('-=-'*20)
    print('Analisando os valores...')
    for valor in num:
        print(f'{valor}', end=' ')
        sleep(0.4)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Ao todo foram informados {cont} valores.')
    print(f'O maior valor foi: {maior}!')


# Programa principal
maior(2, 9, 4, 6, 7, 12)
maior(4, 7, 0)
maior(6)
maior()