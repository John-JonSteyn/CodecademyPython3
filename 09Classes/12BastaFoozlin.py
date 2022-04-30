# CodeCademy Python 3 Course
# Project 12: Basta Fazoolin' with My Heart
# Classes

class Business:
  def __init__(self, name, franchises):
    self.name       = name
    self.franchises = franchises


class Franchise:
  def __init__(self, address, menus):
    self.address  = address
    self.menus    = menus

  def __repr__(self): return self.address

  def available_menus(self, time):
    menus_available = []
    for menu in self.menus:
      if (menu.start_time <= time) and (time <= menu.end_time):
        menus_available.append(menu)
    return menus_available



class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name       = name
    self.items      = items
    self.start_time = start_time
    self.end_time   = end_time
  
  def __repr__ (self):
    return self.name + " menu available from " + str(self.start_time) + " to " + str(self.end_time)

  def calculate_bill(self, purchased_items):
    total = 0
    for item in purchased_items:
      total += self.items[item]
    return total



# Items
arepas_menu = {
  'arepa pabellon': 7.00,
  'pernil arepa'  : 8.50,
  'guayanes arepa': 8.00,
  'jamon arepa'   : 7.50
}

brunc_items = {
    'pancakes'    :  7.50,
    'waffles'     :  9.00,
    'burger'      : 11.00,
    'home fries'  :  4.50,
    'coffee'      :  1.50,
    'espresso'    :  3.00, 
    'tea'         :  1.00,
    'mimosa'      : 10.50,
    'orange juice': 3.50
  }

early_bird_itmes = {
  'salumeria plate'                             :  8.00,
  'salad and breadsticks (serves 2, no refills)': 14.00,
  'pizza with quattro formaggi'                 :  9.00,
  'duck ragu'                                   : 17.50,
  'mushroom ravioli (vegan)'                    : 13.50,
  'coffee'                                      :  1.50,
  'espresso'                                    :  3.00
}

dinner_items = {
  'crostini with eggplant caponata' : 13.00,
  'ceaser salad'                    : 16.00,
  'pizza with quattro formaggi'     : 11.00,
  'duck ragu'                       : 19.50,
  'mushroom ravioli (vegan)'        : 13.50, 
  'coffee'                          :  2.00,
  'espresso'                        :  3.00
}

kids_items = {
  'chicken nuggets'             :  6.50,
  'fusilli with wild mushrooms' : 12.00,
  'apple juice'                 :  3.00
}



# Menus
arepas      = Menu('Arepa'      , arepas_menu       , 1000, 2000)
brunch      = Menu('Brunch'     , brunc_items       , 1100, 1600)
early_bird  = Menu('Early Bird' , early_bird_itmes  , 1500, 1800)
dinner      = Menu('Dinner'     , dinner_items      , 1700, 2300)
kids        = Menu('Kids'       , kids_items        , 1100, 2100)

basta_menu_collection = [
  brunch, early_bird, dinner, kids
]



# Fancises
flagship_store  = Franchise("1232 West End Road"     , basta_menu_collection)
new_installment = Franchise("12 East Mulberry Street", basta_menu_collection)
arepas_place    = Franchise("189 Fitzgerald Avenue", arepas_menu)



# Business
basta = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])
arepa = Business("Take a' Arepa", [arepas_place])


# Output
print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
print(flagship_store.available_menus(1700))
