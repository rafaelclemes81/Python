from random import randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib

navegador = webdriver.Chrome('chromedriver.exe')
navegador.get('https://web.whatsapp.com/')

while len(navegador.find_elements_by_id('side')) < 1:
    time.sleep(1)

#Login feito no whatsapp começa a enviar as msg

lista = [5548991275067, 5548991275067, 5548991275067, 5548991275067, 5548999999999]
#lista = [5548991275067, 5548996109062, 5548999000664, 5548999345157, 5548999999999]

for i in range(1,5):
    if i <= 4:
        numero = lista[i]
    t = randint(7,15)
    texto = urllib.parse.quote('Olá}! Teste de envio de msg pelo whatsapp')
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    navegador.get(link)
    time.sleep(t)
    navegador.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]/button').send_keys(Keys.ENTER)
    time.sleep(t)
    print('Mensagem {} enviada ...'.format(i))
print('Todos as mensagens foram enviadas ... ')
