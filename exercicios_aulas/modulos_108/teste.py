# adaptar e criar uma função moeda() que mostre os valores monetários formatados
import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Se aplicarmos um aumento de 10% a {p}, teremos {moeda.moeda(moeda.aumentar(p,10))}. ')
print(f'Se aplicarmos uma diminuição de 15% a {p}, teremos {moeda.moeda(moeda.diminuir(p,15))}. ')