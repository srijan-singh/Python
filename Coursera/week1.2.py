max = int(input())
elements = input()
elements = elements.split()
list = []
for i in elements:
    list.append(int(i))
list.sort()
result = list[-1] * list[-2]
print(result)