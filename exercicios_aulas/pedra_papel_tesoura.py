from random import randint
from time import sleep #importando a função para esperar
itens = ('pedra','papel','tesoura')
computador = randint(0,2)
#para testar o random e como mostrar o nome:
#print('O computador escolheu {}'.format(itens[computador]))
print('''Suas opções:
[0] -> PEDRA
[1] -> PAPEL
[2] -> TESOURA''')
jogador = int(input('Qual sua Jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!')
sleep(1)
print('-=-' * 10)
print('O computador escolheu {}'.format(itens[computador]))
print('O jogador escolheu {}'.format(itens[jogador]))
print('-=-' * 10)
if computador == 0: #jogou PEDRA
    if jogador == 0:
        print('EMPATE! :|')
    elif jogador == 1:
        print('VOCÊ VENCEU! :D')
    elif jogador == 2:
        print('COMPUTADOR VENCEU :P')
    else:
        print('Jogada INVÁLIDA!')
elif computador == 1: #jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCEU :P')
    elif jogador == 1:
        print('EMPATE! :|')
    elif jogador == 2:
        print('VOCÊ VENCEU! :D')
    else:
        print('Jogada INVÁLIDA!')
elif computador == 2: #jogou TESOURA
    if jogador == 0:
        print('VOCÊ VENCEU! :D')
    elif jogador == 1:
        print('COMPUTADOR VENCEU :P')
    elif jogador == 2:
        print('EMPATE! :|')
    else:
        print('Jogada INVÁLIDA!')