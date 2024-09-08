#PIZZA
pizzas = ['peperoni', 'margarita', 'four cheez']
for pizza in pizzas:
    print(f"i like {pizza} pizza ")
print("I really like pizza!")

#ANIMALS
animals = ['cat', 'tigr', 'leopard']
for animal in animals:
    print(f"A {animal} would make a great pet")
print("Any of these animal would make a great pet!")

friend_pizzas = pizzas[:]
pizzas.append('fritata')
friend_pizzas.append('laluhi')
print("My favorite pizzas are:")
for piz1 in pizzas:
    print(piz1)
print("My friend`s favorite pizzas are:")
for piz2 in friend_pizzas:
    print(piz2)