# Escreva um programa que leia um número inteiro positivo do teclado e informe se ele é par
# ou é impar. Nota: um número é par se o mesmo é divisível por dois, isto é, se o 
# resto da divisão do número por 2 é 0.

numero = int(input("Digite um número: "))

if numero%2 == 0:
    print('Número par!')
else:
    print('Número impar!')