def solution(index):
    primeString = primeString10005()
    return primeString[index:index+5]

def primeString10005():
    primeString = '2357'

    num_list = [3,5,7]

    isPrime = True

    for i in range(9,30000,2):
        
        if (len(primeString) >= 10005):
            break
        
        for j in num_list:
            if i%j == 0:
                isPrime = False
                break
            isPrime = True
        
        if isPrime == True:
            #print(i)
            num_list.append(i)
            primeString += str(i)

    return primeString

print(solution(0))
