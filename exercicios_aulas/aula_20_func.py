# exercícios 96 -100
#
#Fazer (com funções): 96, 97, 99 e 100 (se der)
#
# 97 - programa que tenha função escreva() que recebe texto como parametro
# e mostra mensagem com tamanho adaptável

def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f' a soma de {valores} é {s}')


#Programa Principal
soma(4, 7)
soma(12, 9, 8, 44, 98, 1)
#podemos também explicitar as variáveis
# por exemplo
#soma(a=5,b=7)

def contador(* num):
    tam = len(num)
    print(f'Recebi os valores {num} e são, ao todo, {tam} números')
    print()# print() vazio é para pular uma linha


contador(3, 7, 8)
contador(17, 33, 44, 68)
contador(2, 4, 9, 3, 5, 7, 9)