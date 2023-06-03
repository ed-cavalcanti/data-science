# HOF (High Order Function)

kmh = [10, 20, 30, 40, 50, 60, 70, 80]

# Aplicar um conjnto de dados a umfa função, ou seja, passar por cada elemento e realizar alguma coisa

mph = list(map(lambda x: x/1.61,kmh))

print(mph)

# Utilizando list comprehension

mph2 = [x/1.61 for x in kmh]
print(mph2)