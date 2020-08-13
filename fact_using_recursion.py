''' Here we get the factorial value by using recursion method '''

done = [i for i in range(22)]

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)

print(fact(5))
