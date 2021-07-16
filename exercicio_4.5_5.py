# Faça um programa que leia um conjunto de números positivos do teclado e informe se algum número do conjunto é múltiplo de 10. 
# Assuma que o usuário não sabe com quantos números deseja entrar, de modo que seu programa deve ler números indefinidamente 
# até o usuário entrar com o primeiro número negativo, marcando assim o final da entrada. Note que esse último número negativo não 
# faz parte do conjunto de entrada, e só tem a finalidade de indicar quando os dados acabam. 
# Obs: você deve ler TODOS os números que o usuário digitar até o mesmo entrar com o primeiro valor negativo!

##############################################################################################################
i = int(input('Entre com o número 1 do conjunto: '))

if i%10 == 0:
    x = 'Existe'
else:
    x = 'Não existe'

k = 1

while i >= 0:
    k += 1
    i = int(input(f'Entre com o número {k} do conjunto: '))
    if i%10 == 0:
        x = 'Existe'
    else:
        if x == 'Existe':
            x = 'Existe'
        else:
            x = 'Não existe'

print(f'{x} múltiplo de 10 nesse conjunto!')