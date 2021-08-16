def solution(arr):
    # Terminate condition
    arr[-1][-1] = 3    
    printer(arr)
    result = move_count(arr)
    return result

def move_count(arr, i=0, j=0, count=0):

    if arr[i][j] == 3:
        return count+1
    
    arr[i][j] = 2

    move_arr = get_moves(arr,i,j)

    while move_arr:
        m = move_arr.pop()

        x = m[0]
        y = m[1]

        if (arr[x][y] == 0) or (arr[x][y] == 3):
            return move_count(arr, x, y, count+1)

def get_moves(arr,i,j):
    result = []
    high = len(arr)
    low = -1

    if (i+1 < high):
        if (arr[i+1][j] == 0) or (arr[i+1][j] ==3):
            result.append([i+1,j])
    if (j+1 < high):
        if (arr[i][j+1] == 0) or (arr[i][j+1] == 3):
            result.append([i,j+1])
    if (i-1 > low):
        if (arr[i-1][j] == 0) or (arr[i-1][j] ==3):
            result.append([i-1, j])
    if (j-1 > low):
        if (arr[i][j-1] == 0) or (arr[i][j-1] == 3):
            result.append([i,j-1])
    return result

def printer(arr):
    print('***')
    for i in arr:
        print(i)
    print('***')


#a = solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])
#print(a)
printer([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]])
#printer([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])

