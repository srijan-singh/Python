def frag(lists):

    count = 0
    for list in lists:
        if "KICK" in list:
            count+=1
        if "START" in list:
            count+=1
        if "KICKSTART" in list:
            count+=1

    return count
        
list=[]
x = int(input())
for _ in range(x):
    y = input()
    list.append(x)

print(frag(list))