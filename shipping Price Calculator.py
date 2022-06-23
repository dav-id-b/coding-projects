#This code helps the user determine which of three shipping options is the most economical, based on the weight of their package

weight = 11

#Ground Shipping prices by pound + $20 flat charge
print('Ground Shipping Price: ')

if weight <= 2:
  cost = weight * 1.5 + 20
  print(cost)

elif weight > 2 and weight <= 6:
  cost = weight * 3 + 20
  print(cost)

elif weight > 6 and weight <= 10:
  cost = weight * 4 + 20
  print(cost)

else:
  cost = weight * 4.75 + 20
  print(cost)

#Premium Ground shipping flat charge
print('Premium Ground Shipping Price: ')

pgs = 125
print(pgs)

#Drone Shipping prices by pound - no flat charge
print('Drone Shipping Price: ')

if weight <= 2:
  cost = weight * 4.5
  print(cost)

elif weight > 2 and weight <= 6:
  cost = weight * 9
  print(cost)

elif weight > 6 and weight <= 10:
  cost = weight * 12
  print(cost)

else:
  cost = weight * 14.25
  print(cost)
