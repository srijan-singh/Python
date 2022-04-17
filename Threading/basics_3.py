import threading
import time

def count_x(n):
    for i in range(1, n+1):
        print(i)
        time.sleep(0.01)

def count_y(n):
    for i in range(1, n+1):
        print(i)
        time.sleep(0.02)


x = threading.Thread(target=count_x, args=(10,))
x.start()

y = threading.Thread(target=count_y, args=(10,))
y.start()

print("Done")