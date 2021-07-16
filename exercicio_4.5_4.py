# Faça um programa que calcule o fatorial de um número inteiro lido do teclado.

#########################################################################################################
n = int(input('Digite o Fatorial de: '))
f = 1 #fatorial

print(f'{n}! = ', end='') #o end='' é para evitar que pule linhas.

while n > 0:
    print(f'{n}', end='')
    if n > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
    f *= n
    n -= 1
print(f'{f}')