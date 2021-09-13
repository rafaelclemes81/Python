mt = float(input('Informe o tamanho em metros: '))
print('O valor {} possui {:.0f}cm e {:.0f}mm'.format(mt,(mt*100),(mt*1000)))
print('O valor {} equivale a {:.5f}km, {:.5f}hm e {:.5f}dam'.format(mt, mt/1000, mt/100, mt/10))

