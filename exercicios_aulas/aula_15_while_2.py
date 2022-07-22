# Desafios 66 ao 71
# Fazer = (66(abaixo), 69 e 70 (cadastro de compras)
# 67 - tabuada - 68 - par ou impar - jogo
# 71 - caixa eletrônico simulado - quantas cédulas
#
# ABAIXO é o desafio 66 -
# Um contador que soma todos os números digitados
n = s = cont = 0 # estamos INICIALIZANDO as variáveis
while True:
    n = int(input('digite um número: '))
    if n == 999:
        break
    cont += 1
    s += n
#print('a soma de todos os números é {} '.format(s))
# F STRING - antes das aspas, coloque "f" minusculo
print(f'a soma dos {cont} valores digitados é: {s}')
# interpolação entre strings