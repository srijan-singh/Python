import threading
import time

ls = []

def count_x(n):
    for i in range(1,n+1):
        ls.append(i)
        time.sleep(0.5)

def count_y(n):
    for i in range(1,n+1):
        ls.append(i)
        time.sleep(0.5)

x = threading.Thread(target=count_x, args=(5,))
x.start()

y = threading.Thread(target=count_y, args=(5,))
y.start()

time.sleep(0.9)
print(ls)

time.sleep(0.29)
print(ls)

time.sleep(2)
print(ls)


