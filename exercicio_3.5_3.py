# Escreva um programa que leia os comprimentos dos lados de um triângulo
# e informe se o triângulo é equilátero, isósceles ou escaleno.

lado_1 = input("Digite o comprimento do primeiro lado do triangulo: ")
lado_2 = input("Digite o comprimento do segundo lado do triangulo: ")
lado_3 = input("Digite o comprimento do terceiro lado do triangulo: ")


if lado_1 == lado_2 and lado_2 == lado_3:
    print("Este triângulo é equilátero.")

elif lado_1 != lado_2 and lado_1 != lado_3 and lado_2 != lado_3:
    print('Este trinângulo é escaleno.')

elif lado_1 == lado_2 and lado_2 != lado_3 or lado_1 == lado_3 and lado_1 != lado_2 or lado_2 == lado_3 and lado_2 != lado_1:
    print('Este triângulo é isósceles')
  
# uma outra forma para representar seria, na linha 15, colocar ELSE: <tab> print('Este triângulo é isósceles.')