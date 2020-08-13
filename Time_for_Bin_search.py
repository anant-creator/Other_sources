''' A Programe which shows how binary search works '''

def found(ar, d):
    l = ar[0]; h = ar[-1]
    mid = l + h / 2
    if mid == d:
        print("Found It!")
    elif mid > d:
        h = mid
    elif mid < d:
        l = mid


found(done, 20) '''

