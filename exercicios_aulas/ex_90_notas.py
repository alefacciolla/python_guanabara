# Programa que leia nome e média de um aluno,
# guardando em um dicionário as infos
# ao final, mostre o conteúdo na tela
aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Nota MÉDIA de {aluno["nome"]} é: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-=-'*20)
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')

