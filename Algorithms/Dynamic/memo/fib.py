# Dynamic Programming 
# Divide problems into sub problems
# Find base cases 
# Find a brute force solution of the sub problem
# Sum up the sub solution into general solution
# Optimise the general solution 

"""
# Unoptimised Solution

def fib(n):
    if(n==0):
        return 0
    if (n==1):
        return 1
    return fib(n-1) + fib(n-2)
    """

# Optimised Solution

def fib(n, memo={}):
    # Memoization
    if n in memo:
        return memo[n]

    if(n==0):
        return 0
    if (n==1):
        return 1

    memo[n] = fib(n-1) + fib(n-2)

    return memo[n]


print(fib(2))
print(fib(8))
print(fib(36))
print(fib(62))