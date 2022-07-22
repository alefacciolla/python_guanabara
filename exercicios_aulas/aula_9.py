# "Cadeia de caracteres", "string" ou "cadeia de texto"
# cada caracter é um miniespaço

#FATIAMENTO quer dizer pegar um pedaço
frase = 'curso em video Python'
print(frase[9:13]) #começa no 9 e vai até o 12, pois o último é excludente
#podemos
#print(frase[9:21:2]) #aqui eu mando um RANGE de 9 a 20, PULANDO de 2 em 2
#print(frase[:5]) #vai do 0 a até o 5
#print(frase[15:]) #de 15 até o final
#abaixo, outro jeito de fazer pra ir pulando
#print(frase[9::3]) #primeiro mostra do 9 até o fim e depois, pula de 3 em 3

#Analise
print(frase.count('o',0,13)) #fazendo uma contagem já com fatiamento
#                 ou seja, entre o 0 e o 12
print(frase.find('deo')) #onde começa
#se colocarmos um valor de string que não existe, retorna -1
# IMPORTANTE
print('curso' in frase) #dá para ver se existe a string na frase
#substituindo uma por outra
#frase.replace('python','android')
#frase.upper() #vai jogar tudo para maiúscula
# lower() para minúscula
# captalize() pega a string e transforma em maiúscula só a primeira letra da string
# title() - transforma TODAS as primeiras letras das palavras em maiúscula
# strip() - retira todos os espaços inúteis!
#pode-se usar um r antes da função para que ela comece pela DIREITA
# ex: frase.rstrip() #aqui, tira só da direita, do final
# para o contrário, ESQUERDA, tem o l

# DIVISÃO
#frase.split() ocorrer uma divisão levando os espaços em consideração
# cada palavra é colocada com uma nova indexação
#  JUNÇÃO
# 'separador'.join(frase)

# PARA IMPRIMIR UM TEXTO LONGO

#use TRÊS (3) aspas
#exemplo
print("""Com Paolla Oliveira à frente da bateria
 e uma constelação de famosos espalhados pelas alas,
  incluindo os ex-BBBs Gil do Vigor e Camilla de Lucas,
   a Grande Rio também aproveitou o desfile para combater a intolerância religiosa no Brasil
   .... - Veja mais em
    https://www.uol.com.br/carnaval/
    noticias/redacao/2022/04/26/desencantou-grande-rio-vence-carnaval-do-
    rio-pela-primeira-vez.htm?cmpid=copiaecola""")