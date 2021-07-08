# Um trem de longa distância parte de uma estação inicial em um determinado horário H1 (hora e minuto) 
# e chega à estação final em um determinado horário H2 . 
# Faça um programa em Python que leia os horários de partida e chegada do trem e informe o tempo total de viagem (em hora e minuto)
# Assuma que as viagens sempre iniciam e terminam no mesmo dia.

# entende-se por hp a hora da partida e mp o minuto da partida
# entende-se por hc a hora da chegada e mc o minuto da chegada
# -> LEVAR EM CONTA SOMENTE A PARTIR DA LINHA 27

hp = 10
mp = 35

hc = 11
mc = 25

temp_viagem = ((hc-hp),":",(mc-mp))

print("Hora da partida:", hp)
print("Minuto da partida:", mp)
print("Hora da chegada:", hc)
print("Minuto da chegada:", mc)
print("O trem partiu as", hp, ":", mp, "e chegou as", hc, ":", mc)
print("Tempo de viagem:", temp_viagem)

###################################################################################################
# - Fazendo a diferença entre horas: 11-10 = 1h e sabendo que 1h = 60minutos
# - Fazendo a diferença entre minutos: 35-25 = 10minutos 

hp = 10
mp = 35
hc = 11
mc = 25
hora_e_min_partida = ("10:35")
hora_e_min_chegada = ("11:25")
dif_hora = 60
dif_min = 10

temp_viagem = (dif_hora - dif_min)

print("Hora da partida:", hp)
print("Minuto da partida:", mp)
print("Hora da chegada:", hc)
print("Minuto da chegada:", mc)
print("O trem partiu as", hora_e_min_partida, "e chegou as", hora_e_min_chegada)
print("Tempo de viagem:", "00:",temp_viagem,"minutos")
