# A Bachatóvia adota a Tabela 3.5 para o cálculo do seu imposto de renda.
# Faça um programa que peça a renda anual de um contribuinte e calcule o
# seu devido imposto, de acordo com a tabela

renda = float(input('Digite a sua renda anual: '))

if renda >= 0 and renda <= 21450.00:
    print(f'Imposto: {renda*0.15}')
elif renda > 21450.00 and renda <= 51900.00:
    print(f'Imposto: {renda * 0.028 + 3117.50}')
elif renda > 51900.00:
    print(f'Imposto: {renda * 0.31 + 11743.00}')
else:
    print('Renda inválida!')