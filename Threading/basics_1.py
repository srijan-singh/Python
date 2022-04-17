import threading
import time

def func():
    print('A')
    time.sleep(1)
    print('B')
    time.sleep(0.85)
    print('D')

x = threading.Thread(target=func, args=())
x.start()
print(threading.active_count())
time.sleep(1.2)
print('C')