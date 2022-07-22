from menu.lib.interface import *
from menu.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'
if not arqExiste(arq):
    criArq(arq)

#cabeçalho('SISTEMA ARQUIVO v0.1')
while True:
    resposta = menu(['1 - Ver Pessoas cadastradas', '2 - Cadastrar nova Pessoa', '3 - Sair do sistema'])
    if resposta == 1:
        lerArq(arq)
        # opção de listar o conteúdo de um arquivo.
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)

