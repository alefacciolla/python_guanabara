# usando a estrutura do try para evitar erros de Exceção
#
#Exercícios - 113 - Leiaint() para possibilidade de digitar um número inválido
# faça o mesmo para leiaFloat()
#15 cadastrar pessoas com modularizaçao pedindo idade e nome
#
#fazer: 113, 114 (pudim), 115 (3 partes - manipulação de arquivos)
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:
    print(f'Problema encontrado foi {erro.__class__}')
else:
    print(f'O resultado é {r:.2f}')
finally:
    print('Volte Sempre, valeu! :D')