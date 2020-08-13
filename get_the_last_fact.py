''' here we just find out the last desired factorial amount '''

def fact(x):
    tree = 1
    while x > 0:
        tree *= x
        x -= 1
    print(tree)
