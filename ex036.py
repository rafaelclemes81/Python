"""PROGRAMA PARA APROVAR UM EMPRÉSTIMO BANCÁRIO PARA A COMPRA DE UMA CASA. O PROGRAMA VAI PERGUNTAR O VALOR DA CASA, O SALÁRIO DO COMPRADOR E EM QUANTOS
	ANOS SERÁ PAGA. CALCULE O VALOR DA PRESTÃÇÃO SABENDO QUE NÃO PODERÁ ULTRAPASSAR 30% DO SALÁRIO, OU ENTÃO O EMPRÉSTIMO SERÁ NEGADO."""
valor = float(input('Informe o valor da casa desejada: R$'))
prazo = int(input('Em quantas parcelas você pretende financiar sua casa ? '))
sal = float(input('Informe o seu salário: R$'))
prestacao = valor // prazo
if prestacao > (sal * 30 / 100):
    print('Seu salário de {:.2f} não é compatível com a prestação calculada de R${:.2f}. Seu financiamento não foi aprovado.'.format(sal, prestacao))
else:
    print('A prestação da sua casa será de {:.2f}. Parabéns, seu finaciamento foi aprovado!!!'.format(prestacao))
