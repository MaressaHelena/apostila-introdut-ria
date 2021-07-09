# Escreva um programa que leia as coordenadas do centro de um círculo (em um plano cartesiano) 
# juntamente com o seu raio, e então informe se um determinado ponto de teste lido está dentro do círculo, 
# no centro do círculo, na circunferência (fronteira) ou fora do círculo. 
# Assuma que não ocorrem erro de arredondamento nos cálculos e que o usuário sempre fornece valores válidos. 
# Apenas para lembrar, a equação da circunferência é dada por: (x-xc)²+(y-yc)² = r², 
# onde (xc,yc) são as coordenadas do centro da circunferência e r é o raio. 
# Lembre-se de que seu programa deve informar em qual das quatro categorias está o ponto de teste.

##################################################################################################
xc = float(input('Digite a coordenada x do centro do círculo: '))
yc = float(input('Digite a coordenada y do centro do círculo: '))
r = float(input('Digite o raio do círculo: '))
print("\n**************************\n")
px = float(input('Digite a coordenada x do ponto de teste: '))
py = float(input('Digite a coordenada y do ponto de teste: '))
distancia = ((px-xc)**2 + (py-yc)**2)**(1/2)

#circunferência = (((x-xc)**2 + (y-yc)**2) = r**2)

if distancia < r:
    print('O ponto de teste se encontra dentro do círculo.')
elif distancia > r:
    print('O ponto de teste se encontra fora do círculo.')
elif distancia == r:
    print('O ponto de teste se encontra na circunferência.')
elif distancia == 0:
    print('O ponto de teste se encontra no centro do círculo.')
else:
    print('')