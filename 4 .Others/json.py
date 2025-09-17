import json

# Converte uma string JSON em um dicionário Python

# Converter para string JSON
x_json = '{"nome": "Mario", "idade": "82"}'

# Dicionário Python
x_dicio = json.loads(x_json)
print(x_dicio)

# Converte um dicionário Python para uma string JSON

# Dicionário Python
y_dicio = {"nome": "Mario", "idade": "82"}

# Converter para string JSON
y_json = json.dumps(y_dicio)

print(y_json)