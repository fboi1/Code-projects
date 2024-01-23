import logging
import threading
import time
import concurrent.futures
import multiprocessing 

def thread_function(name):
    print("Thread %s: starting", name)
    #time.sleep(2)
    print("Thread %s: finishing", name)
    for i in range (6):
        print(i)

def threadfunc2():
    print("no")

if __name__ == "__main__":

    process1 = threading.Thread(target=thread_function, args=(1,))
    process2 = threading.Thread(target=threadfunc2)
    for i in range(6):
        print(i)

    process1.start()
    process2.start()
    