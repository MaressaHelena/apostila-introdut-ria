# Em uma conceituada universidade, o sistema de ingresso prevê provas de X disciplinas escolhidas de acordo com a carreira desejada.
# Para conseguir passar por uma entrevista e pleitear uma das vagas da universidade, cada candidato precisa obter grau igual ou 
# superior que 5.0 em todas as provas e apresentar média final maior ou igual que 7.0 considerando todas as notas. 
# Escreva um programa em Python que leia as X notas de um candidato e informe sua média e se ele está apto a prosseguir na disputa
# pelas vagas. ATENÇÃO: Todas as X notas do candidato devem sempre ser lidas. Assuma que todas as entradas sempre serão válidas.
###############################################################################################################################


numProvas = float(input('Entre com o número de provas: '))
contador = 1 #contador
sumNotas = 0

while contador <= numProvas:
    nota = float(input(f'entre com a nota da prova {contador}: '))
    contador += 1
    condicao = 'passou'
    if nota >= 5:
        if condicao == 'reprovou':
            condicao = 'reprovou'
        else:
            condicao = 'passou'
    else:
        condicao = 'reprovou'
    sumNotas += nota
    
media = sumNotas/numProvas

print(f'Média das notas: {media}')

if condicao == 'passou' and media >= 7:
    print('Este aluno está apto ao curso.')
else:
    print('Este aluno não está apto ao curso.')