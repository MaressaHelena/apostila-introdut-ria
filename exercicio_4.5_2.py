# Escreva um programa que leia um número positivo do teclado e informe se ele é par ou ímpar 
# (assuma que o usuário sempre entrará com números inteiros). 
# Seu programa deve tratar o caso em que o número lido é não positivo, informando uma mensagem de erro e 
# solicitando o número novamente até que ele seja válido. Ao final da execução, 
# seu programa deve perguntar ao usuário se ele deseja executar o programa novamente. 
# Se o usuário entrar com o número zero, ele estará dizendo que não, e se entrar com qualquer outro número, 
# estará dizendo que sim. Neste último caso, seu programa deve solicitar novamente a entrada e 
# executar até o usuário não querer mais.
############################################################################################################


n = int(input('Entre com um número: '))

while n < 0:
    print('Insira um número positivo!')
    n = int(input('Entre com um número: '))

else:
    if n%2 == 0:
        print(f'{n} é par!')
    else:
        print(f'{n} é ímpar!')
        
condiçao = int(input('Deseja continuar? (0 - NÃO) (1 - SIM): '))

while condiçao == 1:
    n = int(input('Entre com um número: '))
    while n < 0:
        print('Insira um número positivo!')
        n = int(input('Entre com um número: '))
    if n%2 == 0:
        print(f'{n} é par!')
    else:
        print(f'{n} é ímpar!')
    condiçao = int(input('Deseja continuar? (0 - NÃO) (1 - SIM): '))

else:
    print('Tenha um bom dia!')