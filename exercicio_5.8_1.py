# Faça um programa que leia uma string do teclado e informe a quantidade de caracteres alfabéticos maiúsculos na string


texto = input('Entre com um texto: ')
numero_maiusculo = 0

for c in texto:
    if 'A' <= c <= 'Z':
        numero_maiusculo += 1

print(f'Número de caracteres maiúsculos: {numero_maiusculo}')