# Ler nome e peso de várias pessoas
temp = [] #criando uma lista temporária
principal = []
maior = menor = 0
while True:
    temp.append(str(input('digite seu nome: ')))
    temp.append(float(input('digite seu peso em Kilos (KG): ')))
    if len(principal) == 0:
        maior = menor = temp[1] #a posição 1 dá o peso, que é o que queremos
    else:
        if temp[1] > maior:
            maior = temp[1]
        elif temp[1] < menor:
            menor = temp[1]
    principal.append(temp[:])
    temp.clear()
    resp = str(input('quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('=-='*20)
print(f'Os dados foram {principal}')
# a) Quantidade de pessoas cadastrada
print(f'voce cadastrou {len(principal)} pessoas')
# b) A pessoa mais pesada
# - Para isso, preciso ter o maior e menor peso
print(f'a pessoa cadastrada mais PESADA tem {maior} Kg, peso de:', end='')
for p in principal:
    if p[1] == maior:
        print(f'{p[0]}')
print()
print(f'a pessoa cadastrada mais LEVE tem {menor} Kg, peso de: ', end='')
for p in principal:
    if p[1] == menor:
        print(f'{p[0]}')
# c) Menor peso

