cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_driven = drivers
cars_not_driven = cars - drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print 'There are', cars, 'cars available'
print 'there are only', drivers, 'drivers available'
print 'there will be', cars_not_driven, 'empty cars today'
print 'We can transport', carpool_capacity, "people today"
print "we need about", average_passengers_per_car, "in each car."