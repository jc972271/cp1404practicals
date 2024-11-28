"""CP1404 - Testing unreliable car class."""

from unreliable_car import UnreliableCar

my_car = UnreliableCar("Box on wheels", 1000, 80)
number_of_success = 0

for i in range(99):
    previous_odometer = my_car._odometer
    my_car.distance = 0
    my_car.drive(10)
    #print(my_car)
    if my_car._odometer > previous_odometer:
        number_of_success += 1

print(f"Started {number_of_success}/100")