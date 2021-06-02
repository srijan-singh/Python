def left(arr):
    mid = len(arr)//2
    return arr[:mid]

def right(arr):
    mid = len(arr)//2
    return arr[mid:] 

def merge_sort(arr):

    if (len(arr) > 1):
        
        left_arr = left(arr)
        right_arr = right(arr)

        merge_sort(left_arr)
        merge_sort(right_arr)

        i=j=k=0

        while i<len(left_arr) and j<len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i+=1
            else:
                arr[k] = right_arr[j]
                j+=1
            k+=1

        while i<len(left_arr) and k<len(arr):
            arr[k] = left_arr[i]
            k+=1
            i+=1

        while j<len(right_arr) and k<len(arr):
            arr[k] = right_arr[j]
            k+=1
            j+=1

    return arr    


arr = [13,6,5,2,0,9,1]

print(merge_sort(arr))

