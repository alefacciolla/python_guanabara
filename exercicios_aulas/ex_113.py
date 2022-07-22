# Reescreva a Função leiaInt(),
# incluindo a possibilidade da digitação de um número de tipo inválido.
#Aproveite e crie também a função leiaFloat() com a mesma funcionalidade
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO:  Por valor, digite um número inteiro válido.\033[m')
            continue #o contínue manda voltar para o início do laço, while no caso
        except (KeyboardInterrupt):
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            break
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO:  Por valor, digite um número real válido.\033[m')
            continue #o contínue manda voltar para o início do laço, while no caso
        except (KeyboardInterrupt):
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            break
        else:
            return n


n1 = leiaInt('Digite um valor inteiro: ')
n2 = leiaFloat('Digite um valor real: ')
print(f'O valor inteiro é: {n1}\n'
      f'O Valor real: {n2}')
