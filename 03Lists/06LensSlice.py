# CodeCademy Python 3 Course
# Project 06: Len's Slice
# Lists

toppings = [
  "pepperoni",
  "pineapple",
  "cheese",
  "sausage",
  "olives",
  "anchovies",
  "mushrooms"
]

prices = [
  2,
  6,
  1,
  3,
  2,
  7,
  2
]

num_two_dollar_slices = prices.count(2)
print("The number of USD2 pizzas we have: " + str(num_two_dollar_slices))

num_pizzas = len(toppings)
print("\nWe sell " + str(num_pizzas) + " different kinds of Pizza!")

pizza_and_prices = [
  [2,  "pepperoni"],
  [6,  "pineapple"],
  [1,  "cheese"],
  [3,  "sausage"],
  [2,  "olives"],
  [7,  "anchovies"],
  [2,  "mushrooms"]
]

pizza_and_prices.sort()

print("\nOur menu:")
print(pizza_and_prices)

cheapest_pizza = pizza_and_prices[0]
print("\nOur cheapest pizza:")
print(cheapest_pizza)

priciest_pizza = pizza_and_prices[-1]
print("\nOur pricest pizza:")
print(priciest_pizza)

print("\n" + priciest_pizza[-1] + " has been sold out.")
pizza_and_prices.pop()
priciest_pizza = pizza_and_prices[-1]
print("Our current most expensive pizza is: ")
print(priciest_pizza)

pizza_and_prices.append( [2.5, "peppers"] )
pizza_and_prices.sort()
print("\nAnother pizza has been added to our menu:")
print(pizza_and_prices)

three_cheapest = pizza_and_prices[:3]
print("\nOur cheapest three pizzas are: ")
print(three_cheapest)