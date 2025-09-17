import json

# É necessário criar um arquivo .json com [] dentro.
aluno2 = {"nome":"Jao", "idade" : 20}

from datetime import datetime

dt = datetime.now()

aluno = {"nome":input('Digite seu nome: '), "idade":int(input('Digite sua idade: ')), "horario": str(dt.hour) + ":" + str(dt.minute) }

with open("alunos.json") as j:
    x = json.load(j)
    x.append(aluno)
    
with open("alunos.json", "w") as i:
    i.write(json.dumps(x))