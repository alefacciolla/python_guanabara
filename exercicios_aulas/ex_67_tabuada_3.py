while True:
    n = int(input('Quer ver a tabuada de qual número? '))
    if n <= 0:
        break
    print('-='*25)
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
    print('-=' * 25)
print('Programa TABUADA encerrado, volte sempre! :D')