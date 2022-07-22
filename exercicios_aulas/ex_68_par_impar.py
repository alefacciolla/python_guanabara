from random import randint
v = 0 #inicializando a contagem de vitórias
while True:
    jogador = int(input('digite um valor entre 0 e 10 '))
    computador = randint(0,11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI': #ou seja, enquanto não for Par ou Impar
        tipo = str(input('Par [P] ou Ímpar [I]? ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador, {computador}.\n'
          f'total de {total}')
    print('\nDeu PAR!' if total % 2 == 0 else 'Deu ÍMPAR!')
    if tipo == 'P':
        if total % 2 == 0:
            print('O resultado é par! Você ganhou!')
            v += 1 #contando número de vitórias
        else:
            print('Que pena, você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('O resultado é impar, você venceu!')
            v += 1
        else:
            print('Que pena, você perdeu!')
            break
        print('vamos jogar novamente...')
print('=-=' * 15)
print(f'GAME OVER. Você venceu {v} vezes!\n'
      f' Até a próxima!')
print('=-=' * 15)
