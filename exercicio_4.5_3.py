# Escreva um programa que leia um conjunto de números (termos) do teclado e imprima o produto de todos 
# esses números. Antes de começar a ler os números, o programa deve solicitar o total de termos que o 
# usuário pretende entrar. Não se esqueça de que um produtório de 0 termos deve resultar em zero.
#######################################################################################################

numTermos = int(input('Entre com o número de termos: '))
produto = 1

if numTermos > 0:
    for k in range(0, numTermos):
        termo = float(input(f'Entre com o termo {k+1}:'))
        produto *= termo 
        
    print('Produtorio: ', produto)

elif numTermos == 0:
    print('Produtório: ', numTermos*0)
