# adaptar para que as funções aceitem um parametro a mais
#informando se o valor retornado vai ser ou não formatado pela função moeda()
import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Se aplicarmos um aumento de 10% a {p:.0f}, teremos {moeda.aumentar(p,10, True)}. ')
print(f'Se aplicarmos uma diminuição de 15% , teremos {moeda.diminuir(p,15, True)}. ')