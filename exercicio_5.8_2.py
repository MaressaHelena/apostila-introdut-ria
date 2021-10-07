# Faça um programa que leia uma string do teclado e imprima essa mesma string com os caracteres alfabéticos com caixa invertida, isto é, os caracteres maiúsculos devem ser impressos minúsculos e os maiúsculos devem ser impressos minúsculos

texto = input('Entre com o texto: ')
texto_invertido = texto.swapcase()
print(f'O texto invertido é: {texto_invertido}')