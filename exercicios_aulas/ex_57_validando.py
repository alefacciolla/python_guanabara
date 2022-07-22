sexo = str(input('Informe seu sexo [M/F] ')).strip().upper()[0]
#aqui tiramos os espaços.strip(), deixamos em maiúsculo e
# pegamos só a primeira letra digitada
#como não sabemos quantas vezes será feita essa pergunta, usamos:
while sexo not in 'MF':
    sexo = str(input('Dados Inválidos.\n'
                     'por favor,tente novamente - [M] - Masculino'
                     ' ou [F] - Feminino')).strip.upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))
print(sexo)
#idade = int(input('Informe sua idade '))