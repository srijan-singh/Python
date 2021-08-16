# Queue it's a user defined data structure which follows FIFO
from collections import deque
my_queue = deque()
# enqueue is used with append
my_queue.append(5)
my_queue.append(10)
print(my_queue)
# dequeue is used with popleft
print(my_queue.popleft())

