# Programa com uma tupla com várias palavras
palavras = ('python', 'programacao', 'linguagem',
            'trabalho', 'musica', 'zen')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos as vogais: ')
    for letra in p:
        if letra.lower() in 'aeiyou':
            print(letra, end=' ')
#depois, mostrar, para cad palavra, quais sãoas vogais
# print(f'as vogais {} ')