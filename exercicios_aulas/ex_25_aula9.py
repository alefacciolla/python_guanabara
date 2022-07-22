# programa que leia o nome da pessoa e diga se tem 'Silva'
nome = str(input('qual seu nome completo? ')).strip()
print('seu nome tem Silva? {}'.format('SILVA' in nome.upper()))