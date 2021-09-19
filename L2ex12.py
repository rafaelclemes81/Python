'''Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
mas não é descontado (é a empresa que deposita).
O Salário Líquido corresponde ao Salário Bruto menos os descontos.
 O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20%
Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00'''

vlr = float(input('Informe o valor da hora: '))
horas = float(input('Informe quantas horas foram trabalhadas: '))
bruto = horas * vlr
sindicato = bruto * (3 / 100)
fgts = bruto * (11 / 100)
inss = bruto * (10 / 100)

if bruto <= 900:
    descontos = bruto + sindicato + ir + inss
    liquido = bruto - descontos
elif bruto <= 1500:
    percir = 5
    ir = bruto * (percir / 100)
    descontos = sindicato + ir + inss
    liquido = bruto - descontos
elif bruto <= 2500:
    percir = 10
    ir = bruto * (percir / 100)
    descontos = sindicato + ir + inss
    liquido = bruto - descontos
else:
    percir = 20
    ir = bruto * (percir / 100)
    descontos = sindicato + ir + inss
    liquido = bruto - descontos

print(f'{" Cálculo de Folha de pagamento ":-^51}')
print(f'{"Salário Bruto ":.<40} {bruto:>10.2f}')
print(f"{'(-IR) ({percir}%)':.<40}{ir:>10.2f}")
print(f'{"(-Sindicato) (3%)":.<40}{sindicato:>10.2f}')
print(f'{"FGTS (11%)":.<40}{fgts:>10.2f}')
print(f'{"(-INSS) (10%)":.<40}{inss:>10.2f}')
print(f'{"Total de Descontos":.<40}{descontos:>10.2f}')
print(f'{"Salário líquido":.<40}{liquido:>10.2f}')

