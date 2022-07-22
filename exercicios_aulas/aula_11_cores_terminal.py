# códigos ANSI - escape sequence -
# cores
#\033[m
#entre o [ e o m vai o código da cor
# 3 códigos: style, text e background

# códigos para ESTILO no python começam com:
# 0 (nada), 1(negrito), 4(sublinhado) ou 7(inverter)

#para TEXTO: de 30 a 37

# para BACKGROUND de 40 a 47

print('\033[4:30:41mOlá, mundo!\033[m') #fundo vermelho e sublinhado
# abri e fechei a configuração

#MANEIRA MAIS FÁCIL

nome = 'Ale Facciolla'
#print('Olá, muito prazer, {}{}{}'.format('\033[30:41m',nome,'\033[m'))
# nas chaves {} antes de depois, códigos de cores

#Também podemos fazer um DICIONÁRIO com
# chave Nome da cor e valor o código daquela cor
cores = {'limpa':'\033[m', 'azul':'\033[34m'}
#daí é só chamar pela chave
print('Olá, muito prazer, {}{}{}'.format(cores['azul'],nome, cores['limpa']))
