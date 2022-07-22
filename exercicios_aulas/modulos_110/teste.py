# adaptar para que as funções aceitem um parametro a mais
#informando se o valor retornado vai ser ou não formatado pela função moeda()
import moeda

p = float(input('Digite o preço: R$ '))
moeda.resumo(p, 20, 13) #resumo do preço, com 20% de aumento e 13% de desconto
