# Special XOR Property
def special_xor_property(a):
    res = [
        a,  
        1,
        a+1,
        0
        ]

    return res[a%4]

# Get Xor from any range within O(log n)
def getXor(inital, final):
    return special_xor_property(final)^special_xor_property(inital-1)
    

def solution(num, range_to):
    if range_to == 1:
        return num

    max_range = num + range_to**2
    #print("Max Range ",max_range) #correct

    current_num = num
    range_setter = 0
    result = 0
	

    while(current_num < max_range):
        
        # Final Valid Number
        new_range = current_num + range_to - range_setter -1

        if range_to == range_setter:
            break

        #print(current_num, new_range)  
        xor_range = getXor(current_num, new_range)
        
        result ^= xor_range

        # Increment
        current_num+=range_to
        range_setter+=1

    return result

if __name__ == "__main__":
   
    print(solution(17, 4))
    
    """
    Approached used:
    
    print(17^18^19^20) = 4
    print(21^22^23) = 20
    print(25^26) = 3
    print(29) = 29
    
    print(4^20^3^29) => Answer
    """
    #print(solution(2000000000, 20000))
    #print(solution(2000000000, 2000000)) #67753902080