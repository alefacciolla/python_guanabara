#para criar uma lista vazia podemos fazer
# assim: valores = []
# ou
# valores = list()
num = [4,8,9,3,2]
num[1] = 10 # para mudar
num.append(7) #para adicionar
num.sort(reverse=True) # para ficar na ordem descrescente
num.insert(2, 0) #inserindo 2 na posição 0
num.remove(2) #elimina o valor 2 na primeira vez que aparece
print(num)
print(f'essa lista tem {len(num)} elementos.')

