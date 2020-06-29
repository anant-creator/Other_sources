''' calculate the sum of the digits of a randon 3 digit number '''


from random import random

num = random() * 900 + 100
num = int(num)
print(num)

a = num // 100
b = (num // 10) % 10
c = num % 10

print(a + b + c)
