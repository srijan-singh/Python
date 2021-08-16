def solution(arr):
    result_arr = max_div_3(arr)
    result = ""
    for i in result_arr:
        result += str(i)
    return result
        
def max_div_3(arr):
    # Rearranging list in ascending order to remove the smallest number if necessary
    arr.sort()

    arr_sum = sum_up(arr)    

    remainder = arr_sum % 3

    # Divisibilty rule of 3
    if remainder == 0:
        # Rearranging list in descending oreder to get the biggest number
        arr.reverse()
        return arr

    # List of all indivisible numbers
    indv_num_arr = indv_num(arr)

    # Removing the smallest indivisible numbers
    arr = pop_small_indv(indv_num_arr, remainder, arr)

    # Rearranging list in descending oreder to get the biggest number
    arr.reverse()

    return arr

def sum_up(arr):
    arr_sum = 0
    for i in arr:
        arr_sum += i
    return arr_sum

def indv_num(arr):
    indv_num_arr = []
    for i in arr:    
        indv_num_arr.append(i%3)
    return indv_num_arr

def pop_small_indv(indv_num_arr, remainder, arr):

    pop_index_low, pop_index_high = num_finder(indv_num_arr, remainder)

    # If only one number has to pop
    if pop_index_low == pop_index_high:
        arr.pop(pop_index_low)

    # If more numbers has to be pop
    elif pop_index_low != pop_index_high:

        # List containing pop element
        pop_list = []

        # Adding element to the list
        for i in range(pop_index_low, pop_index_high+1):
            pop_list.append(arr[i])

        # Poping the indivisible element 
        for i in pop_list:
            if i%3!=0:
                arr.remove(i)

    return arr

def num_finder(arr, target, low=0, high=1):
    # Out of Range
    if (low<0 or high>len(arr) or low>high):
        return -11, -10

    num_sum = 0

    for i in range(low,high):
        num_sum += arr[i]

    # Target Found
    if num_sum == target:
        return low, high-1

    elif num_sum < target:
        return num_finder(arr, target, low, high+1)

    else:
        return num_finder(arr, target, low+1, high)

print(solution([7,5,5,4,3,1]))
print(solution([3, 1, 4, 1]))
print(solution([3, 1, 4, 1, 5, 9]))
print(solution([]))
print(solution([9, 9, 9, 9]))

