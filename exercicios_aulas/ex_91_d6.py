# não precisa de nenhum dado do leitor
# 92 - crie programa no qual 4 jogadores jogam um D6 com resultados aleatórios
# Guarde o resultado em um dict().
from time import sleep
from random import randint
from operator import itemgetter
jogo = { 'jogador1': randint(1, 6),
         'jogador2': randint(1, 6),
         'jogador3': randint(1, 6),
         'jogador4': randint(1, 6)}
ranking = {}
print(f'valores sorteados foram: ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-='*20)
print(' === RANKING DOS JOGADORES ===')
#print(ranking) #aqui dá o resultado em uma lista com tuplas dentro com k e v
for i, v in enumerate(ranking):
    print(f'    {i+1}º lugar: {v[0]} com {v[1]}')
    # o i+1 é pq o índice começa em 0
    sleep(1)
# ao final, coloque o dict() em ordem, sabendo que o vencedor tirou o maior número
#mostre o ranking - para isso, precisamo criar outro dicionário, de ranking


