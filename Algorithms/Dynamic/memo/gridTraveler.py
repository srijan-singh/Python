# Dynamic Programing
# Divide problem into sub problem
# Find base case
# Find brute force solution for sub problems
# Sum up sub problems
# Optimised solution

"""

# Unoptimised Solution

def gridTraveler(m,n):

    if (m == 0 or n == 0):
        return 0

    if (m == 1 and n == 1):
        return 1

    return gridTraveler(m-1, n) + gridTraveler(m, n-1)
"""

def gridTraveler(m,n,memo={}):
    
    key = str(m)+','+str(n)

    if key in memo:
        return memo[key]

    if (m==0 or n==0):
        return 0

    if (m==1 and n==1):
        return 1

    memo[key] = gridTraveler(m-1, n, memo) + gridTraveler(m, n-1, memo)

    return memo[key]


print(gridTraveler(1, 1))
print(gridTraveler(3, 4))
print(gridTraveler(8, 9))
print(gridTraveler(21, 16))