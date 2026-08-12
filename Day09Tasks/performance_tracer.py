# Q14 :Performance Tracker (Decorators) 
# A software team wants to track how long functions take to execute. Create a decorator 
# that measures and prints the execution time of a function. 
import time
def track_time(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("Execution time:", end - start, "seconds")
    return wrapper
@track_time
def task():
    print("Task is running...")
    time.sleep(2)
task()
    