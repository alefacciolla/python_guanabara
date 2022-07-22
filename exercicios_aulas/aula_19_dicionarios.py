# Exercícios 90 a 95
# 91 - 4 jogadores, um dado (D6) e resultados aleatórios
# a) Guarde em um dicionário e, no final,
#coloque o dicionário em ordem. O vencedor tirou o n mais alto
# 92 - nome, ano de nasc, carteira de t. e cadastre, com idade, em um dict().
# Fazer 90, 91, 92, 94 (SE DER)
pessoas = {'nome': 'Alexandre', 'sexo': 'M', 'idade': 35}
for k, v in pessoas.items():
    print(f'{k} = {v}')
#não se acha pelo índice, mas pelo nome da chave
# para fazer formatado, precisa usar aspas diferentes na chave
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
#na hora de referenciar, usa colchetes [].
# para declarar, chaves {}
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items()) #lista composta por 3 tuplas, é o resultado
#para mudar um valor, digite o nome do dict, colchetes e o nome da chave
#como abaixo
#pessoas['nome'] = 'Luis'
# para adicionar um novo elemento, é do mesmo jeito