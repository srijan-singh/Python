import threading
import time

def count(n):
    for i in range(1, n+1):
        print(i)
        time.sleep(0.01)

for thr in range(2):
    x = threading.Thread(target=count, args=(10,))
    x.start()

print("Done")