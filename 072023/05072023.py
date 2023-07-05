from collections import deque

class OrderLog:
    def __init__(self, size):
        self.log = deque(maxlen=size)
    
    def record(self, order_id):
        self.log.append(order_id)
    
    def get_last(self, i):
        if i <= len(self.log):
            return self.log[-i]
        else:
            return None


log = OrderLog(5)  # Initialize with a log size of 5

log.record(1001)
log.record(1002)
log.record(1003)
log.record(1004)
log.record(1005)
log.record(1006)  # The oldest order_id (1001) is dropped from the log

print(log.get_last(1))  # Output: 1006
print(log.get_last(3))  # Output: 1004
print(log.get_last(5))  # Output: 1002
print(log.get_last(6))  # Output: None (log size is 5)
