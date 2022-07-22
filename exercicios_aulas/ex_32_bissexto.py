#ano bissexto tem que ser divisível por QUATRO e
# ocorre a cada 4 anos
#   exceto em anos múltiplos de 100 que NÃO SÃO múltiplos de 400

# não pode ser divisível por 100 ou por 400
from datetime import date
ano = int(input('Digite um ano e saiba se é BISSEXTO,\n'
                ' ou digite 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('o ano {} É bissexto'.format(ano))
else:
    print('o ano {} NÃO É bissexto'.format(ano))