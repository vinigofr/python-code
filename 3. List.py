# Sequencia mutavel e ordenada de elementos. Pode armazenar
# elementos heterogeneos, tem tamanho variavel e cresce a
# medida que se adicionam elementos.

fruits = ["orange", "apple", "grape", "pineapple"] # Declaração

fruits[0]  # Acesso

fruits[-1]  # o acesso também pode ser negativo (Para acessar o ultimo elemento)

fruits.append("banana")  # adicionando uma nova fruta

fruits.remove("pineapple")  # removendo uma fruta

fruits.extend(["pear", "melon", "kiwi"])  # acrescenta uma lista de frutas a lista original

fruits.index("apple")  # retorna o índice onde a fruta está localizada, neste caso 1 em seu programa

fruits.sort()  # ordena a lista de frutas

# Praticando:
trybe_course = ["Introdução", "Front-end", "Back-end"]

trybe_course.append("Ciência da Computação") # Adicione o elemento "Ciência da Computação" à lista.
print(trybe_course)

trybe_course[0] = "Fundamentos" # Acesse e altere o primeiro elemento da lista para "Fundamentos".
print(trybe_course)
