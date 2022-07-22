# pedir lista com 5 elementos, mostrar os números e
# dizer os valores max e min
listanum = []
maior = 0
menor = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para posição {c} ')))
    if c == 0: #ou seja, quando for o primeiro valor lido
        maior = menor = listanum[c] #na posição c
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        elif listanum[c] < menor:
            menor = listanum[c]
print('-=-'*20)
print(f'Voce digitou os seguintes valores {listanum}')
print('-=-'*20)
print(f'O valor MAIOR foi {maior}, encontrado nas posições ', end='')
for i, v in enumerate(listanum):
    if v == maior:
        print(f' {i}...')
print('-=-'*20)
print(f'O valor MENOR foi: {menor}, encontrado nas posições ', end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f' {i}...')
print('-=-'*20) #para quebrar linha
#len(listanum)
