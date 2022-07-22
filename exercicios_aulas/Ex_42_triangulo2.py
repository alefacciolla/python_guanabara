#Ex 42
#mostrar se o triângulo é
# EQUILÁTERO: todos os lados iguais
# ISÓSCELES: dois lados iguais
# ESCALENO: todos os lados diferentes
print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('os segmentos PODEM FORMAR um Triângulo ', end='')
#o end='' dentro de print puxa o print debaixo p/ mesma linha
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 and r2 != r3 and r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Os segmentos NÃO PODEM formar um Triângulo.')