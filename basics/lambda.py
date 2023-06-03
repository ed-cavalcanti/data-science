# Forma tradicional de declarar uma função
def somaQuadrados(num1, num2):
    return num1 ** 2 + num2 ** 2

print(somaQuadrados(2, 3))

# Utilizando função lambda
# Forma de declarar uma função anônima, sem encessidade de dar um nome a ela

somaQuadradosL = lambda num1, num2: num1 ** 2 + num2 ** 2

print(somaQuadradosL(2, 3))