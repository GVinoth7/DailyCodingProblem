# Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
import time

def sched_func(f, n):
    time.sleep(n/1000)
    f()
    
# Example 
def my_function():
    print("Job executed !")
    
sched_func(my_function, 5000)

def job_scheduler(f,n):
    time.sleep(n/1000)
    f()
    
    
job_scheduler(lambda: print("Job executed!"), 500) #