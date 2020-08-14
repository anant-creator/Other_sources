''' Here we have created a algorithem to sort a list using selected sort '''


arru = [5, 3, 7, 4, 9, 8, 2]

def sorting(arr):
    for i in range(len(arr)-1):
        minpos = i
        for j in range(i, len(arr)):
            if arr[minpos] > arr[j]:
                minpos = j

        temp = arr[minpos]
        arr[minpos] = arr[i]
        arr[i] = temp

    print(arr)

sorting(arru)
