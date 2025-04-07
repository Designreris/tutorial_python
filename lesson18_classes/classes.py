# PYTHON CLASSES - Blueprints for objects

class Vehicle:
  def __init__(self, make, model):
    self.make = make
    self.model = model

  def moves(self):
    print('Moves along...')

  def get_make_model(self):
    print(f"I'm a {self.make} {self.model}.")
  


my_car = Vehicle('Tesla', 'Model 3')

# print(my_car.make, my_car.model)
# my_car.get_make_model()
# my_car.moves()

your_car = Vehicle('VW', 'Golf')
# your_car.get_make_model()
# your_car.moves()
#############################################

# INHERITANCE

class Airplane(Vehicle):
  def __init__(self, make, model, faa_id):
    super().__init__(make, model)
    self.faa_id = faa_id

  def moves(self):
    print('Flies along...')

class Truck(Vehicle):
  def moves(self):
    print('Rumbles along...')

class GolfCart(Vehicle):
  pass

cessna = Airplane('Cessna', 'Skyhawk', 'N-1234')
mack = Truck('Mack', 'Pinnacle')
golf_cart = GolfCart('Yamaha', 'GC100')

# cessna.get_make_model()
# cessna.moves()
# mack.get_make_model()
# mack.moves()
# golf_cart.get_make_model()
# golf_cart.moves()
######################################

# POLYMORPHISM - Ability to behave differently to the same input.

print('\n\n')

for v in (my_car, your_car, cessna, mack, golf_cart):
  v.get_make_model()
  v.moves()
