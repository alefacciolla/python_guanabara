# 97 - programa que tenha função escreva() que recebe texto como parametro
# e mostra mensagem com tamanho adaptável
def escreva(txt):
    print('~'*(len(txt) + 4)) #posso colocar isso em outra variável, tipo tamanho
    print(f'  {txt}')
    print('~' * (len(txt) + 4))


#Programa principal
escreva('roberta')
