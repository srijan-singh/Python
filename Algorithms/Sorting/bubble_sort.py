def linear_sort(arr):
    for i in range(len(arr)-1):
        if (arr[i] > arr[i+1]):
            temp = arr[i+1]
            arr[i+1] = arr[i]
            arr[i] = temp        
    return arr

def bubble_sort(arr):
    arr = linear_sort(arr)
    for i in range(len(arr)-1):
        if (arr[i] > arr[i+1]):
            return bubble_sort(arr)
    return arr


if __name__ == "__main__":
    
    user_input = input("Enter Length of the List: ")
    length = int(user_input)

    arr = []

    for num in range(length):
        user_input = input("Enter Element {} : ".format(num+1))
        arr.append(int(user_input))

    print("Given List: ",arr)

    bubble_sort(arr)

    print("Sorted List: ",arr)


