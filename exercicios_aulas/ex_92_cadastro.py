# programa que leia nome, ano de nascimento e carteira de trabalho
# cadastre-os (com idade) em um dict().
# se a CTPS for != de 0, dict() receberá o ano de contratação e salário
# calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar
# DICIONÁRIO COM TAMANHO VARIÁVEL
from datetime import datetime
dados = {}
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de trabalho [digite 0 se não tiver]'))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-=-'* 20)
for k, v in dados.items():
    print(f'  - {k} tem o valor {v}')
