# 5 valores em input e colocar em lista
# já na posição correta de incerção no índice
# SEM USAR SORT()
# - Mostre, no final, a lista ordenada na tela
lista = []
for c in range(0,5): #lembrando que o 5 é desconsiderado
    n = int(input('digite um valor'))
    if c == 0 or n > lista[-1]:
#ou seja, se for o primeiro valor ou maior que o último elemento
        lista.append(n)
        print(f'adicionado ao final da Lista...')
    else:
        posicao = 0
        while posicao < len(lista): #vai do 0 à última posição
            if n <= lista[posicao]:
                lista.insert(posicao, n)
                print(f'adicionado na posição: {posicao} ')
                break
            posicao += 1 #ou seja, entra na frente da posição de n
print('-='*30)
print(f'Os valores digitados em ordem foram {lista}')


