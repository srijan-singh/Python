def factorial(n):
    if n==1:
        return 1

    return n * factorial(n-1)

print(factorial(56))

# Time: O(n)
# Space: O(n)