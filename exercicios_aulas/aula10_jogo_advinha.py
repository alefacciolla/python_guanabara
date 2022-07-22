# ex 28 - escrever um programa que faça o computador pensar
# RANDOMICAMENTE e um número inteiro entre 1 e 5 e peça para o usuário
#descobrir qual foi. O programa deve mostrar na tela se o user ganhou ou perdeu.
# opicional: mostrar o número que "pensou"
from random import randint
from time import sleep #importando a função para esperar
computador = randint(0, 5)
print('-=-' * 25)
print('vou pensar em um número entre 0 e 5. Advinhe...se puder')
print('-=-' * 25)
#print('pensei no número {}'.format(computador)) #faz computador sortear
jogador = int(input('Qual número entre 0 e 5 eu pensei? ')) #jogador tenta advinhar
print('PROCESSANDO...')
sleep(2) # durma 2 segundos
if jogador == computador:
    print('parabéns, vc acertou!')
else:
    print('Nessa eu ganhei!hehe.\n'
          ' Pensei no número {}\n'
          'e não no {}!'.format(computador, jogador))
