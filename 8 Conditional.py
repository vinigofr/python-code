# Sintaxe de estrutura condicional

salary = 1000
position = ""
if salary <= 2000:
    position = "estagiário"
elif 2000 < salary <= 5800:
    position = "júnior"
elif 5800 < salary <= 7500:
    position = "pleno"
elif 7500 < salary <= 10500:
    position = "senior"
else:
    position = "líder"

# Em alguns casos, que não prejudiquem a legibilidade, podemos criar estruturas de mapeamento ( dicts ) para simplificar o aninhamento de condicionais.

key = "id"
from_to = {
    "id": "identifier",
    "mail": "email",
    "lastName": "last_name",
}
from_to[key]