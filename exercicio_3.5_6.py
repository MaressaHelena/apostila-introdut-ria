# Faça um programa para calcular a média final de um aluno da matéria de 
# Abstração I da Universidade da Bachatóvia. As provas dessa universidade 
# são pontuadas de 0 a 10, podendo haver casas decimais nas notas. 
# A média final deve ser calculada segundo as regras abaixo

# (a) O programa deve receber inicialmente dois números representando 
# as notas da Prova 1 (P1) e da Prova 2 (P2) do aluno. Se a média M1 = (P1+P2)/2 
# for maior ou igual que 7,0, o aluno estará aprovado direto.
# Se essa mesma média for menor que 3,0, o aluno estará reprovado direto. 
# Nesses dois casos, esta média M1 será a média final do aluno.

# (b) Caso a média M1 do aluno fique entre 3,0 e 7,0, o aluno deve realizar uma Prova Final (PF). 
# Apenas nesse caso, o programa deverá pedir também a nota da PF. A média final MF será então calculada
# segundo a expressão MF = (M1+PF)/2, onde M1 é a média calculada entre a P1 e a P2 no item anterior.
# Para este último caso, se MF for maior ou igual que 5,0, o aluno estará aprovado.
# Caso contrário, estará reprovado.

##########################################################################################################

P1 = float(input('Digite a nota da P1:'))
P2 = float(input('Digite a nota da P2:'))

if P1 >= 0 and P1 <= 10 and P2 >= 0 and P2 <= 10:
    media = round((P1+P2)/2, 2)
    if media >= 7:
        print(f'Situação: Aprovado direto! Média final: {media}')
    if media < 3:
        print(f'Situação: Reprovado direto! Média final: {media}')
    if 3 < media < 7:
        Pf = float(input('Digite a nota da PF:'))
        f = (media + Pf)/2
        if f > 5:
            print(f'Situação: Aprovado! Média final: {f}')
        else:
            print(f'Situação: Reprovado! Média final: {f}')
else:
    print('Nota inválida!')