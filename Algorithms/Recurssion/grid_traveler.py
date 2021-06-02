def gridtrav(a,b, memo={}):
    
    key = (a,b)

    sorted(key)

    if key in memo:
        return memo[key]

    if a==1 and b==1:
        return 1

    if a==0 or b==0:
        return 0

    memo[key] = gridtrav(a-1, b, memo) + gridtrav(a, b-1, memo)

    return memo[key]

print(gridtrav(18,18))

