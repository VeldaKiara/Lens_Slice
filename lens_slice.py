#pizza joint
toppings = ['pepperoni','pineapple','cheese','sausage','olives','anchovies','mushrooms']
prices = [2,6,1,3,2,7,2]
num_pizzas = len(toppings)
print('We sell {} different kinds of pizza!'.format(num_pizzas))
pizzas = list(zip(toppings,prices))
print(pizzas)
pizzas.sort()
cheapest_pizza = pizzas[0]
