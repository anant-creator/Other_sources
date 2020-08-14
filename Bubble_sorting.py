''' Today we have created Bubble sorting :) '''


arru = [5, 3, 7, 4, 9, 8, 2]
def bubble(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                k = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = k
    return arru    


print(bubble(arru))
