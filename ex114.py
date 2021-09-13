''' CRIE UM CÓDIGO EM PYTHON QUE MOSTRE SE DETERMINADO SITE ESTÁ ACESSÍVEL'''

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.uol.com.br')
except urllib.error.URLError:
    print('O site pudim não está acessível no momento.')
else:
    print('Consegui acessar o site com sucesso')