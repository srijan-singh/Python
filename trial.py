def solution(src, dest):
    source = [int(src)]
    result = SP(source, int(dest))
    return result

def matrix(num = 8):
    arr = []

    for i in range(8):
        sub_arr = []
        for j in range(8):
            sub_arr.append(j + i*8)
        arr.append(sub_arr)

    return arr

def moves(num):
    arr = []
    result = (num-17)
    arr.append(result)
    result = (num-17)+2
    arr.append(result)
    result = (num-10)
    arr.append(result)
    result = (num-10)+4
    arr.append(result)
    result = (num+6)
    arr.append(result)
    result = (num+6)+4
    arr.append(result)
    result = (num+15)
    arr.append(result)
    result = (num+15)+2
    arr.append(result)

    return arr

def num_arr(num,arr,max_value=8):
    for i in range(max_value):
        if arr[i][0] <= num and arr[i][-1] >= num:
            return i

def valid_moves(arr, num, main_arr, min_value = 0, max_value = 7):
    check_arr = [num - 2, num - 1, num + 1, num + 2]

    i = 0
    j = 0

    while i<len(check_arr):

        if(check_arr[i]) < min_value or check_arr[i] > max_value:
            check_arr.pop(i)
            arr.pop(j)
            arr.pop(j)
        else:
            i+=1
            j+=2

    i = 0
    j = 0
    
    while i<len(check_arr) and j<len(arr)-1:
        num_1 = arr[j]
        num_2 = arr[j+1]
        max_value = main_arr[check_arr[i]][7]
        min_value = main_arr[check_arr[i]][0]
        
        value = 0
        if num_1 > max_value or num_1 < min_value and num_2 > max_value or num_2 < min_value:
            value = 2
        elif num_1 > max_value or num_1 < min_value:
            value = 1
        elif num_2 > max_value or num_2 < min_value:
            value = 1.5
        if value == 1:
            arr.pop(j)
            i+=1
            j+=1
        elif value == 1.5:
            arr.pop(j+1)
            i+=1
            j+=1
        elif value == 2:
            arr.pop(j)
            arr.pop(j)
            i+=1
        else:
            i+=1
            j+=2
    
    return arr

def get_moves(num):
    main_arr = matrix()

    move_arr = moves(num)

    target_num = num_arr(num,main_arr)

    valid_move_arr = valid_moves(move_arr, target_num, main_arr)

    return valid_move_arr

def SP(src,target,count=0, q=[]):
    for i in src:
        if i == target:
            return count
        q+= get_moves(i)    
    #print(q)
    new_count = count + 1
    src = []
    #print(src)
    while q:
        for i in q:
            if i == target:
                return new_count
        for i in q:
            temp = q.pop()
            src+=get_moves(temp)
    new_count+=1
    return SP(src,target,new_count)

