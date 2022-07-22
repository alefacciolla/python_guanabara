estado = {}
brasil = []
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa(UF): '))
    estado['sigla'] = str(input('Sigla da UF: '))
    brasil.append(estado.copy())
# print(brasil) ou
for e in brasil: #esse é para a lista
    for k, v in e.items(): #esse, para o dict()
        print(f'O campo {k} = {v}')
    #print(e)