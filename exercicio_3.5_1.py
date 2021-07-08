# Escreva um programa que leia um número inteiro entre 1 e 12 representando um mês e 
# imprima se este mês tem 28, 30 ou 31 dias. Assuma conforme a tabela 3.4 que fevereiro tem 
# 28 dias


mes = input('Digite o numero do mes: ')

if mes in ('1', '3', '5', '7', '8', '10', '12'):
    print('Mes com 31 dias!')

elif mes in ('4', '6','9', '11'):
    print('Mes com 30 dias!')

elif mes in ('2'):
    print('Mes com 28 dias!')

else:
    print("Mes invalido!")
