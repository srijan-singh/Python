def minElement(arr, start, end):
    
    min_element = arr[start]
    
    index = start

    for i in range(start, end):
        if arr[i] < min_element:
            min_element = arr[i]
            index = i
    
    return index


def selectionSort(arr, length):

    for index in range(length):

        smallest = minElement(arr, index, length)
        
        arr[index], arr[smallest] = arr[smallest], arr[index]
    
    return


if __name__ == "__main__":
    user_input = input("Enter Length of the List: ")
    length = int(user_input)

    arr = []

    for num in range(length):
        user_input = input("Enter Element {} : ".format(num+1))
        arr.append(int(user_input))

    print("Given List : ",arr)

    selectionSort(arr, length)

    print("Sorted List : ",arr)