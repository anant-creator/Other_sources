# Return swapcase character code 

def fun(char):
	if char.isalpha():
		print(ord(char.swapcase()))
	else:
		print(ord(char))
		
		
fun("a")
