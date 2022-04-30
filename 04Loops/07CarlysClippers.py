# CodeCademy Python 3 Course
# Project 07: Carly's Clippers
# Loops

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0
for price in prices:total_price += price
average_price = total_price / len(prices)
print("Average Haircut Price: USD " + str(average_price))

new_prices = [price + 5 for price in prices]
print("\nOur new prices:")
for i in range(len(new_prices)):
  print(str(new_prices[i]) + "\t" + hairstyles[i])

total_revenue         = 0
for i in range(len(hairstyles)):
  total_revenue       += prices[i] * last_week[i]
print("\nTotal Revenue: USD " + str(total_revenue))
average_daily_revenue = total_revenue / 7
print("Average Daily Revenue: USD" + str(average_daily_revenue) + "\n")

cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if (prices[i] < 30)]
print("Haircuts under USD30")
for haircut in cuts_under_30:print(haircut)