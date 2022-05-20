def solution(n):
    n = int(n)
    i = 0
    while n > 1:
        if (n&1) == 0:
            n >>= 1
        elif (n&3) == 1 or n == 3:
            n -= 1
        else:
            n += 1
        i += 1
    return i