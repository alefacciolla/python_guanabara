#ler nome completo de uma pessoa e mostrar
# 1 nome com todas as letras e maiúscula
# 2 quantas letras ao #todo (sem espaços)
# 3 quantas letras o primeiro nome
nome = str(input('digite nome completo: ')).strip()
#vai fatiar em uma lista com as strings s/ espaços
print('analisando nome...')
print('seu nome em maiúscula é {}'.format(nome.upper()))
print('seu nome em minúscula é {}'.format(nome.lower()))
print('seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
#print('seu primeiro nome tem {} letras'.format(nome.find(' ')))
#aqui mostra as letras pois acha o primeiro espaço (no find
separa = nome.split()
print('seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))