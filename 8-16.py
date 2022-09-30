# 8.16
import car
car = car.make_car("subaru", "outback", color="blue", tow_package=True)
print(car)

from car import make_car
car = make_car("subaru", "outback", color="blue", tow_package=True)
print(car)

from car import make_car as mc
car = mc("subaru", "outback", color="blue", tow_package=True)
print(car)

import car as cr
car = cr.make_car("subaru", "outback", color="blue", tow_package=True)
print(car)

from car import *
car = make_car("subaru", "outback", color="blue", tow_package=True)
print(car)
