# Um palíndromo é uma palavra ou frase que tenha a propriedade de poder ser lida tanto da direita para a esquerda como da esquerda para a direita com igual significado.
# Em um palíndromo, normalmente são desconsiderados os sinais ortográficos (diacrítico ou de pontuação), assim, como o espaço entre palavras.
# Escreva um palíndromo que leia uma string do teclado e informe se a mesma é um palíndromo. Assuma que a string lida nunca conterá caracteres alfabéticos acentuados 


palindromo = str(input('Digite a frase: ')).strip().upper()
palavra = palindromo.split()
junto = ''.join(palavra)
inverso = ''

for c in range(len(junto) -1, -1, -1): # aqui eu pego o final da string até o inicio da string (como uma contagem regressiva)
    inverso += junto[c] # aqui ocorre a concatenação de string
if inverso == junto:
    print(f'{junto} e {inverso} formam um PALÍNDROMO!')
else:
    print(f'{junto} e {inverso} NÃO formam um PALÍNDROMO!')