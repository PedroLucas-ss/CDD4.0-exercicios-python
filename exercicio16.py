horaInicio = int(input("Digite a hora de inicio do seu jogo(somente a hora sem os minutos): "))
horaFim = int(input("Digite a hora de termino do seu jogo(somente a hora sem os minutos): "))

horaTotal = 0

if horaInicio < horaFim:
    horaTotal = horaFim

elif horaInicio > horaFim:
    horaTotal = (24 - horaInicio) + horaFim

else:
    horaTotal = horaInicio + horaFim

if horaTotal <= 24:
    print(f"seu jogo teve uma duracao de {horaTotal}")
else:
    print("O jogo ultrapassou o limite de 24 horas.")


