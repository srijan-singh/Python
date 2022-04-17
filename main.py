def printer(color, p1, p2, p3):

    p1_value = True
    p2_value = True
    p3_value = True
    
    result = 0
    for i in range(4):
        result+=i
        if color < result:
            p1_value = False
            break
        
    if(p1_value):
        for i in p1:
            print(i, end=" ")
        print()
        return
    
    result = 0
    for i in range(4):
        result+=i
        if color < result:
            p2_value = False
            break
        
    if(p2_value):
        for i in p2:
            print(i, end=" ")
        print()
        return

    result = 0  
    for i in range(4):
        result+=i
        if color < result:
            p3_value = False
            break
        
    if(p3_value):
        for i in p3:
            print(i, end=" ")
        print()
        return
    
    print("IMPOSSIBLE")
    return


test_case = int(input())

for i in range(test_case):
    color = 1000000
    
    pattern1 = list(map(int, input().strip().split()))
    
    pattern2 = list(map(int, input().strip().split()))
    
    pattern3 = list(map(int, input().strip().split()))
    
    printer(color, pattern1, pattern2, pattern3)