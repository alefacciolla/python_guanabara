# 70
# a) programa que leia o nome e preço de vários produtos
# b) deve perguntar se o usuário vai continuar
total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$ '))
    cont += 1 #tinha 0 produtos, agora conto sempre que tiver nome e preço
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O TOTAL da compra foi R$ {total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$ 1.000,00')
print(f'O produto mais barato foi {barato} que custa R$ {menor:.2f}')
# c) mostre:
# 1- total gasto na compra
# 2- quantos produtos > 1000 reais
# 3- produto mais barato