def swap(arr, end):
    for index in range(end, 0, -1):
        if arr[index] < arr[index-1]:
            arr[index], arr[index-1] = arr[index - 1], arr[index]
    return

def insertionSort(arr, length):
    for index in range(1,length):
        swap(arr, index)
    return


if __name__ == "__main__":
    user_input = input("Eneter Length of the List: ")
    length = int(user_input)
    
    arr = []
    
    for num in range(length):
        user_input = input("Enter Element {} : ".format(num+1))
        arr.append(int(user_input))
        
    
    print("Given List: ", arr)

    insertionSort(arr, length)
    
    print("Sorted List: ", arr)