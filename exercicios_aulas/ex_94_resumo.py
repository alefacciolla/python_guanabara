# Aqui é um resumo de dicionários e listas
#Ex_94 - Crie um programa que leia o NOME, SEXO e IDADE de N pessoas.
# dados de cada um guardado em um Dicionário e todos os dicts, em uma LISTA
galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear() #para formar um novo dicionário com a nova pessoa cadastrada
    pessoa['nome'] = str(input('Digite seu nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F]')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        else:
            print('ERRO! digite apenas M (Masculino) ou F (Feminino)')
    pessoa['idade'] = int(input('Idade (anos): '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer Continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=-' * 15)
#print(galera)
# A) quantas pessoas cadastradas
print(f' A) Ao todo temos {len(galera)} pessoas cadastradas.')
# B) Média de idade - quero tentar a mediana, p/ evitar distorções
media = soma / len(galera)
print(f' B) A media das idades foi: {media:3.0f} anos')
# C) Lista com as mulheres cadastradas
print(' C) As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] in 'F':
        print(f'{p["nome"]}', end='')
print()
# D Uma lista com a(s) idade(s) acima da média
print('D) Lista de pessoas com idade acima da média de idade: ', end='')
for p in galera:
    if p['idade'] >= media:
        print('     ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')

