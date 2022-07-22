from menu.lib.interface import cabeçalho


def arqExiste(nome):
    try:
        a = open(nome, 'rt') #rt é read e text, ou seja, leia e escreva
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criArq(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArq(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
        print(a.read())
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')# at é append text
    except:
        print('Houve um ERRO na abertura do arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados.')
        else:
            print(f'Novo registro de {nome} adicionado com sucesso!')
            a.close()

