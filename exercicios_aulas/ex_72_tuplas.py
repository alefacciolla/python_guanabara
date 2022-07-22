
cont = ('zero', 'um', 'dois', 'três', 'quatro','cinco',
        'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
        'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
        'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('digite um número entre 0 e 20 '))
    if 0 <= num <= 20:
       break
    print('tente novamente.\n ', end=' ')
# abaixo, um print FORMATADO - aula 15 mundo 2
print(f'Você digitou o número {cont[num]}')


