def partition(arr, start, end):
    
    pivot = arr[end]

    index = start - 1

    for i in range(start, end):
        if arr[i] < pivot:
            index += 1
            arr[index], arr[i] = arr[i], arr[index]
    
    index += 1
    arr[end], arr[index] = arr[index], arr[end]
    
    return index
    


def quickSort(arr, start, end):
    if start<end:
        pivot_index = partition(arr, start, end)
        quickSort(arr, start, pivot_index-1)
        quickSort(arr, pivot_index+1, end)


if __name__ == "__main__":

    user_input = input("Enter Length of the List: ")
    length = int(user_input)

    arr = []

    for num in range(length):
        user_input = input("Enter Element {} : ".format(num+1))
        arr.append(int(user_input))

    print("Given Array: ", arr)

    quickSort(arr, 0, length-1)

    print("Sorted Array: ", arr)