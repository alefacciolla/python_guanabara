# Exercícios Lista parte 1 - de 78 a 83
# 78 - guardar valores numa lista e mostrar maior e menor com posição na lista
# 79 - vários valores numéricos e coloca numa lista.
# a) Caso o número já exista, não será adicionado
# b) Ao final, todos os valores únicos em ordem crescente

# FAZER: 78, 79, 80, 81, 82(dividindo valores em listas)

# Listas são mutáveis
valores = []
for cont in range(0,5):
    valores.append(int(input('Digite um valor')))
#valores.append(6)
#valores.append(9)
#valores.append(7)
for c,v in enumerate(valores): #aqui a chave vai ser o índice
    print(f'Na posição {c} encontrei o valor {v}')
print('fim da lista')
# lista = ['amora', 'manga', batata']
# lista.append('trigo') - sempre adiciona ao final
#
#CÓPIA DE LISTA
# b = a - em python, isso conecta as listas
# para fazer cópia sem ligar
# b = a[:]    #pegando todos os elementos
# adicionar ítem num lugar específico
# exemplo
# lista.insert(posição, 'item')
## isso vai adicionar uma posição ao índice!

# apagar elementos
# deletando o elemento na posição 3 do índice
# del lista[3]
# OU
# lista.remove('item')

# verificar antes de remover
#if item in lista:
#    lista.remove('item')

# Criar listas através de range
#valores = list(range(4,11))
#print(valores)
# para colocar na ordem, valores.sort()
# para O CONTRÁRIO ordem inversa
# valores.sort(reverse=True)

#len(valores) - útil para fazer laços