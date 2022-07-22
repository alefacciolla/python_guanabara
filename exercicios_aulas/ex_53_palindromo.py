frase = str(input('digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1] #fatiamento, pega de traz pra frente
'''for letra in range(len(junto) - 1, -1, -1):#no fim, -1 é p/ voltar
    inverso += junto[letra]'''
if inverso == junto:
    print('Temos um PALÍNDROMO!:D')
else:
    print('a frase não é um palíndromo :/')
print(junto, inverso)
#se a string tem 10 letras, a última letra,
# pelo índice, é 9. portanto, coloca -1
#print('voce digitou a frase {}'.format(palavras))
