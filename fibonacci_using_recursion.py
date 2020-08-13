''' Here we are going to show you how to get fibonacci using recursion '''


def fib(j):
    if j == 1 or j == 2:
        return 1
    else:
        return fib(j - 1) + fib(j - 2)

print(fib(9))
