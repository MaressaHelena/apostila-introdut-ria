# Escreva um programa que leia um vetor de n coordenadas e informe se o vetor se encontra no primeiro ortante (ortante positivo). 
# Nota: um vetor se encontra no ortante positivo se todas as suas coordenadas são números positivos.
#################################################################################################################################


i = float(input('Entre com o número de coordenadas: '))

c = 1 #contagem

while c <= i:
    u = float(input(f'Entre com a coordenada {c}: ')) # variavel pra eu inserir as coordenadas
    c += 1
    j = 'se encontra'
    if u > 0:
        if j == 'não se encontra':
            j = 'não se encontra'
        else:    
            j = 'se encontra'
    else:
        j = 'não se encontra'
        
print(f'Esse vetor {j} no primeiro ortante')