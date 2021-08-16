def merge(arr, start, mid, end):
    temp = []

    left = start; right = mid+1

    while(left<=mid and right <=end):
        if arr[left] < arr[right]:
            temp.append(arr[left])
            left+=1

        else:
            temp.append(arr[right])
            right+=1

    while(left<=mid):
        temp.append(arr[left])
        left+=1

    while(right<=end):
        temp.append(arr[right])
        right+=1

    for i in range(start, end+1):
        arr[i] = temp[i - start]


def mergeSort(arr, start, end):
    if start < end:
        mid = (start+end)//2
        mergeSort(arr, start, mid)
        mergeSort(arr, mid+1, end)
        merge(arr, start, mid, end)


if __name__ == "__main__":
    user_input = input("Enter Length of the List: ")
    length = int(user_input)

    arr = []

    for num in range(length):
        user_input = input("Enter Element {} : ".format(num+1))
        arr.append(int(user_input))

    print("Given List: ", arr)

    mergeSort(arr, 0, length-1)

    print("Sorted Array: ",arr)