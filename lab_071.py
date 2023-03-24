from time import time

def summation(n):
    return ((n+(n+1))/2)

def loop_sum(n):
    a = 0
    for i in range(1, 1+n):
        a += i
    return a

def analyze_algo(n=1):
    stime = time()
    summation(n)
    etime = time()
    elapsed = etime-stime
    print("execution time: ", elapsed)

analyze_algo(10000000)