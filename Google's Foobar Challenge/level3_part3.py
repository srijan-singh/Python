def solution(n):
    n = int(n)
    count = 0
    while n > 1:
        #If we consider n % 2 == 0, we can replace that modulo entirely with n & 1 == 0, because the bit-pattern of 1 is 0b00000001, which means we will only be looking at the last bit of n (which happens to be the easiest way to determine even vs. odd).
        if (n&1) == 0:
            # 1 bit shift
            n >>= 1
        elif (n&3) == 1 or n == 3:
            n -= 1
        else:
            n += 1
        count += 1
    return count