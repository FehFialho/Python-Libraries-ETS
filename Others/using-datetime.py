from datetime import datetime


# Obter a data e hora atual do computador.
dat = datetime.now() # 2025-05-09 15:05:11.179709
print(dat)

print("Ano: ", dat.year)
print("Mês: ", dat.month)
print("Dia: ", dat.day)
print("Hora: ", dat.hour)
print("Minuto: ", dat.minute)
print("Segundo: ", dat.second)
print("Microsegundo: ", dat.microsecond)

# Outra forma de 
print("\n---- TimeSTR -----")
timestr = dat.strftime("%d-%b-%Y (%H:%M:%S.%f)")
print(timestr)

# Calculo de Diferença de tempo
print("\n---- Diferença -----")
birth = datetime(2006, 2, 2)
idade = dat - birth
print(idade)
