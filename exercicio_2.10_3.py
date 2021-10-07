# Escreva um programa que calcule as duas raízes da equação de segundo grau: ax 2 + bx + c = 0 
# (note que as raízes podem ser exibidas como números complexos). 
# Seu programa deverá ler os valores de a, b e c do teclado. 
# Dica: calcule ∆ = b**2 − 4ac sempre como número complexo

# maisumpeso = complex ( p e s o ) #gera um objeto complex a partir do valor da variavel peso 
# >>> maisumpeso
# >>>(60+0 j)

a = float(input('Entre com o valor de a: '))
b = float(input('Entre com o valor de b: '))
c = float(input('Entre com o valor de c: '))
delta = (b**2) - (4*a*c)
raiz_1 = (-b -(delta)**0.5)/2*a
raiz_2 = (-b +(delta)**0.5)/2*a

delta_c = complex(delta)
raiz1 = complex(raiz_1)
raiz2 = complex(raiz_2)

print(f"Delta: {delta_c}")
print(f"Raizes: {raiz1} e {raiz2}")
