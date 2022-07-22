import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Se aplicarmos um aumento de 10% a {p}, teremos {moeda.aumentar(p,10)}. ')
print(f'Se aplicarmos uma diminuição de 15% a {p}, teremos {moeda.diminuir(p,15)}. ')