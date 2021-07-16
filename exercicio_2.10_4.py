# Hora e minuto de partida
hora_partida = 10
min_partida = 35

# Hora e minuto de chegada
hora_chegada = 11
min_chegada = 25

# Calculando a diferença dos horários em minutos
dif_em_minutos = (hora_chegada*60 + min_chegada) - (hora_partida*60 + min_partida)

# Mas a gente quer algo no formato HH:MM de diferença

HH = (dif_em_minutos - dif_em_minutos%60)/60
MM = dif_em_minutos%60

# Essa % calcula o resto de uma divisão. No caso tá dividindo por 60 e MM vai ser o resto dessa divisão

print("O trem partiu as", hora_partida, ":", min_partida, " | chegou as", hora_chegada, ":", min_chegada)
print("O tempo de viagem foi de", HH, ":", MM)

print()
print("----- MAS AQUI TÁ UMA FORMA DE EXIBIR MAIS BONTINHA E AVANÇADA -----")
print("O trem partiu as {:.0f}:{:.0f} | chegou as {:.0f}:{:.0f}".format(hora_partida, min_partida, hora_chegada, min_chegada))
print("O tempo de viagem foi de {:.0f}:{:.0f}".format(HH, MM), "minutos")