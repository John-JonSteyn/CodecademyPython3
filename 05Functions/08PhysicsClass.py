# CodeCademy Python 3 Course
# Project 08: Physics Class
# Functions

# Convert c, f
def f_to_c(f_temp):
  c_temp = ( (f_temp) - 32) * (5/9)
  return c_temp

def c_to_f(c_temp):
  f_temp = c_temp + (9/5) + 32
  return f_temp

f100_in_celsius = f_to_c(100)
c0_in_fahrenheit = c_to_f(0)
print("100f\t= " + str(round(f100_in_celsius ,2)) + "\tc")
print("0c\t= "   + str(round(c0_in_fahrenheit,2)) + "\tf\n")



# Train m, a
def get_force(mass, acceleration):
  return mass * acceleration

train_mass = 22680
train_acceleration = 10
train_force = get_force(train_mass, train_acceleration)

print("The GE train supplies " + str(train_force) + " N of force.\n")



# Bomb, E
def get_energy(mass, c=3*(10**8)):
  return mass * c

bomb_mass = 1
bomb_energy = get_energy(bomb_mass)
print("A " + str(bomb_mass) + "kg bomb supplies " + str(bomb_energy) + "J\n")



# Train, W
def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration)
  return force * distance

train_distance = 100
train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does " + str(train_work) + "J of work over " + str(train_distance) + "m.")