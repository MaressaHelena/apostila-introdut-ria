# Faça um programa que calcule as raízes reais de uma equação de primeiro
# ou segundo grau. Assuma que a equação estará no formato

# Seu programa deverá receber como entrada os valores dos coeficientes a, b
# e c, e imprimir as raízes reais (se a equação as tiver). Note que quaisquer algarismos podem ser digitados como entrada 
# para a, b e c, e se a = 0, então seu programa deverá calcular uma raiz de equação de primeiro grau.

##############################################################################################################################

a = float(input('Entre com o valor de a: '))
b = float(input('Entre com o valor de b: '))
c = float(input('Entre com o valor de c: '))

delta = (b ** 2) - (4 * a * c)
# x = -c/b para quando a=0 e b!=0

if a != 0:
    delta = (b ** 2) - (4 * a * c)
    if delta >= 0:
        print( 'Raízes:', (-b + delta**(1/2))/(2*a), 'e', (-b - delta**(1/2))/(2*a) )
    else:
        print('Esta equação não possui raízes reais.')
elif b != 0:
    print('Raíz:', -c/b )
else:
    print('Equação inválida!')