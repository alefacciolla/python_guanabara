# advinhação com contagem de palpites
#fazer ainda...
from random import randint
from time import sleep #importando a função para esperar
computador = randint(0, 10)
print('-=-' * 25)
print('vou pensar em um número entre 0 e 10.\n'
      'Advinhe...se puder!')
print('-=-' * 25)
acertou = False
palpites = 0
while not acertou:
      jogador = int(input('Que número entre 0 e 10 eu pensei? '))
      palpites += 1
      print('PROCESSANDO...')
      sleep(1)  # durma 2 segundos
      if jogador == computador:
            acertou = True
      else:
            if jogador < computador:
                  print('Mais... tente de novo')
            elif jogador > computador:
                  print('Menos... tente de novo')
print('Acertou com {} palpites'.format(palpites))
