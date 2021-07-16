# Escreva um programa que receba um número do teclado e informe sua raíz quadrada real. 
# Note que seu programa não deve aceitar números negativos como entrada, de modo que, 
# se o usuário fornecer algum número menor que zero, seu programa deve solicitar o número novamente até o usuário 
# fornecer uma entrada não-negativa.
##################################################################################################################

n = float(input('Digite um número: '))

while n < 0:
    print('Insira valores positivos!')
    n = float(input('Digite um número: '))
else:
    print(f'Raíz quadrada: {n**0.5}')