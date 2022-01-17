# A Sequência de Fibonacci, muito presente em diversas formas na natureza, é uma sequência numérica começando por 0 e 1 e cada termo subsequente corresponde à soma dos dois anteriores.
# Podemos escrever esta sequência da seguinte maneira:

n = 10
last = 0
next = 1

while last < n:
    print(last)
    last, next = next, last + next

# Escreva um código que calcule o fatorial de um número inteiro.

entrada = 5
resultado = 1
for index in range(entrada):
    resultado = resultado * (index + 1)
print(resultado, "resultado")
