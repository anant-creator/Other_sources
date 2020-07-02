''' it multiplies every element of list used as a parameter of a function '''


list = [12, 13, 14, 15, 16, 17, 18, 19]
def five(x):
	return x * 5
	
def new_func(fun, list):
	for i in list:
		print(five(i))
		
new_func(five, list)
