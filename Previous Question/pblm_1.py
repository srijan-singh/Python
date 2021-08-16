def solution(arr, target):

    if len(arr) == 1 and arr[0] == target:
        return 0,0

    net_sum = 0

    for i in range(len(arr)-1):
        net_sum += arr[i]

    if (net_sum < target):
        return -1, -1

    else:

        low,high=target_finder(arr,target)
        return low, high

def target_finder(arr, target, low=0, high=1):

    if (low < 0) or (high > len(arr)) or (high < low):
        return -1, -1

    net_sum = 0

    for i in range(low, high):
        net_sum += arr[i]

    if (net_sum == target):
    
        return low, high-1
    

    elif (net_sum < target):
    
        return target_finder(arr,target,low,high+1)
    
    else:
    
        return target_finder(arr,target,low+1,high)
    

print(solution([250,0,0], 250))
print(solution([1,2,3,4], 15))
print(solution([4, 3, 10, 2, 8], 12))
print(solution([4, 3, 5, 7, 8], 12))
print(solution([260], 260))