# criar pacote chamado utilidades que tenha
#       dois módulos internos
#       chamados: moeda e dado
# Transfira todas as funções para o primeiro pacote e manhtenha tudo funcionando
from modulos_111.utilidades import moeda
from modulos_111.utilidades import dado


p = dado.leiaDinheiro('Digite o preço: R$ ')
moeda.resumo(p, 25, 10)
