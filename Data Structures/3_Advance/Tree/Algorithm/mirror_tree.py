def get_mirror_index(num : int) -> int:
    # Special Case
    if num == 0:
        return num

    if num%2==0:
        return num-1

    return num+1

def mirror_tree(arr_1 : list, arr_2 : list) -> bool:
    length = len(arr_1)
    
    if length != len(arr_2):
        return False
    
    for index in range(length):
        mirror_index = get_mirror_index(index)

        if mirror_index >= length:
            return False

        if (arr_1[mirror_index] != arr_2[index]):
            return False

    return True

if __name__ == "__main__":
    arr_1 = [1,3,2,4,5,6,8]
    arr_2 = [1,2,3,5,4,8,6]

    result = mirror_tree(arr_1, arr_2)

    print(result)