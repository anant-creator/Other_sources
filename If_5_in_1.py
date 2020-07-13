# When 5 person can be fit in a car then how many cars needed


import math as m
def cars(n):
	return m.ceil(n / 5)

c = cars(13)
print(c)
