# crie um código que diga se o site Pudim está acessível
import urllib
import urllib.request
try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('Deu ruim, não está acessível! =o :x')
else:
    print('Jóia :D Acessamos o site Pudim com sucesso')
    print(site.read()) #para ler o conteúdo

