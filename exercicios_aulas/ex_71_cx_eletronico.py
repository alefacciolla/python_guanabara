#simulação caixa eletronico
# pergunte #
# 1 - o valor a ser sacado e
print('='*30)
print('{:^30}'.format('BANCO É NÓIS'))
print('='*30)
valor = int(input('Qual valor vc quer sacar? R$ '))
total = valor
cedula = 50
tot_ced = 0
while True:
    if total >= cedula:
        total -= cedula # vou tentar tirar 50 deste valor
        tot_ced += 1
    else:
        if tot_ced > 0:
            print(f'Total de {tot_ced} cédulas de R$ {cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        tot_ced = 0
        if total == 0:
            break
print('='*30)
print('ACABOU. VOLTE SEMPRE :D')

# 2 - quantas cedulas de cada valor serão entregues
# 2.1 considere que tem cédulas de R$ 50, R$ 20, R$ 10 e R$ 1
