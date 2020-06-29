''' Area and perimeter of a right angle triangle '''


base = int(input("Enter the base of triangle:- "))
height = int(input("Enter the height of triangle:- "))
print("If you want to know the area then use '0' as hypotenuse")
hypotenuse = int(input("Enter the hypotenuse:- "))
area = base * height / 2
perimeter = base + height + hypotenuse
if hypotenuse == 0:
    print(area)
else:
    print(perimeter)
