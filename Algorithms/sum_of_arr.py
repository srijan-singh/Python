def SlowSum(arr):
    # empty array
    if len(arr) == 0:
        return 0
    #excluding the first element
    rest = arr[1:]
    return arr[0] + sum(rest)

# Time O(n^2)
# Space O(n)

def FastSum(arr):
    return _sum(arr,0)
def _sum(arr,idx):
    if idx==len(arr):
        return 0
    return arr[idx] + _sum(arr, idx+1)

# Time O(n)
# Space O(n)

print(FastSum([9,4,6,7,8]))

