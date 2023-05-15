#The following are three functions to determine force, energy, and work using a variety of user-input parameters

def get_force(mass, acceleration):
  return mass * acceleration

def get_energy(mass, c = 3*10**8):
  return mass * c**2

def get_work(mass, acceleration, distance):
  return get_force(mass, acceleration) * distance
