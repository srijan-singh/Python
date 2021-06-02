def bubble_sort(arr):
    arr = linear_sort(arr)
    for i in range(len(arr)-1):
        if (arr[i] > arr[i+1]):
            return bubble_sort(arr)
    return arr

def linear_sort(arr):
    for i in range(len(arr)-1):
        if (arr[i] > arr[i+1]):
            temp = arr[i+1]
            arr[i+1] = arr[i]
            arr[i] = temp        
    return arr

arr = [13,6,5,2,0,9,1]

print(bubble_sort(arr))

