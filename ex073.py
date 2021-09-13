''' CRIE UMA TUPLA PREENCHIDA COM OS 20 PRIMEIROS COLOCADOS DA TABELA DO CAMPEONATO BRASILEIRO DE FUTEBOL,
NA ORDEM DE COLOCAÇÃO. DEPOIS MOSTRE:
A - APENAS OS 5 PRIMEIROS COLOCADOS
B - OS ÚLTIMOS 4 COLOCADOS NA TABELA
C - UMA LISTA COM OS TIMES EM ORDEM ALFABÉTICA
D - EM QUE POSIÇÃO NA TABELA ESTÁ O TIME DA CHAPECOENSE'''
times = 'Palmeiras', 'Atlético MG', 'Fortaleza', 'Bragantino', 'Atlético PR', 'Flamengo', 'Ceará', 'Bahia', 'Fluminense', 'Santos', 'Atlético GO', 'Corinthians', 'Inter', 'Juventude', 'São Paulo', 'Sport Recife', 'América MG', 'Cuiabá', 'Grêmio', 'Chapecoense'
print(f'G5 do Brasileirão: {times[:5]}')
print(f'Z4 do Brasileirão: {times[-4:]}')
print(f'''O times do Brasileirão 2021:
   {sorted(times)}''')
print(f'O time da Chape no momento encontra-se na {times.index("Chapecoense")+1}ª posição')
