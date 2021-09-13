import moeda

p = float(input('Digite o preço do produto: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, formato=True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, formato=True)}')
print(f'Aumentando {moeda.moeda(p)} em 10%, temos {moeda.aumentar(p, 10, formato=True)}')
print(f'Diminuindo {moeda.moeda(p)} em 15%, temos {moeda.diminuir(p, 15, formato=True)}')

