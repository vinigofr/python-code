# Compreensao de lista(equivalente map e filter)

restaurants = [1, 2, 3, 4, 5]

min_rating = 3.0
filtered_restaurants = [restaurant # <- Aqui fica o que sera usado para filtro, e depois gerara o resultado.
    for restaurant in restaurants
    if restaurant["nota"] > min_rating]
print(filtered_restaurants)  # imprime a lista de restaurantes, sem o B e D
