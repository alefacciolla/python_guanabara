# DESAFIOS de 46 a 57
# FAZER: 49, 50, 52, 53, 56
#for c in range(1,7):
#    print(c)
#print('FIM')
# PARA CONTAR PARA TRÁS e
# PULAR, indique depois do range, no 3º elemento
for c in range(7,0,-1): #no forloop, vai TIRANDO 1
    print(c)
print('FIM')
#for c in range(0,7,2):
#    print(c)
#print('FIM')
# OUTPUT
#0
#2
#4
#6
#FIM
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i,f+1,p): #aqui vai de início, ao fim, pulando passo
    print(c)
print('FIM')

#para FAZER UM SOMATÓRIO
s = 0 # s recebe 0
for q in range(0, 5):
    n = int(input('Digite um valor: '))
    s = s + n #ou seja, o valor digitado mais 0
print('A soma foi: {}'.format(s))
