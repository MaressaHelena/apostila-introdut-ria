# Escreva um programa que leia duas strings do teclado e informe se todos os caracteres da primeira string também aparecem na
# segunda 

primeira_string = input('Entre com o primeiro texto: ').upper()
segunda_string = input('Entre com o segundo texto: ').upper()

contador = 0

for letra1 in primeira_string:
    if letra1 in segunda_string:
        contador += 1
        
if contador == len(primeira_string):
    print('Todas as letras do texto 1 constam no texto 2')
elif contador > 0:
    print('Nem todas as letras do texto 1 constam no texto 2')
else:
    print('Nenhuma letra do texto 1 consta no texto 2')