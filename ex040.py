"""040 - CRIE UM PROGRAMA QUE LEIA DUAS NOTAS DE UM ALUNO E CALCULE SUA MÉDIA, MOSTRANDO UMA MSG NO FINAL,
      DE ACORDO COM A MÉDIA ATINGIDA:
	- MÉDIA ABAIXO DE 5.0: REPROVADO
	- MÉDIA ENTRE 5.0 E 6.9: RECUPERAÇÃO
	- MÉDIA 7.0 OU SUPERIOR: APROVADO
"""
print('-' * 20, 'DESAFIO 040', '-' * 20)
n1 = float(input('Informe a 1ª nota: '))
n2 = float(input('Informe a 2ª nota: '))
m = (n1 + n2) / 2
if m < 5:
    print('Você não se esforçou o bastante. Sua média final foi {:.2f}, e você foi reprovado.'.format(m))
elif m < 7:
    print('Você deveria ter se esforçado um pouco mais. Sua média final foi {:.2f} e você está em recuperação'.format(m))
elif m >= 9:
    print('Parabéns!!! Sua média foi {:.2f} e você foi um aluno acima da média e está aprovado.'.format(m))
else:
    print('Sua média foi {:.2f} e você foi aprovado.'.format(m))