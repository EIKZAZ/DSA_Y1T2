import random
from time import time 

def randomList(n):
    a = list(random.sample(range(1,1000000), n))
    b = list(random.sample(range(1000001, 2000000), n))
    c = list(random.sample(range(2000001, 3000000), n))
    return a,b,c

def isIntersect_1(a, b, c):
    for number in a:
        if number in b and number in c:
            return True
        return False

def isIntersect_2(a, b, c):
    for i in range(0, len(a)):    
        for j in range(0, len(b)):
            for k in range(0, len(c)):
                if c[k] == b[j] == a[i]:
                    return True
    return False

def analyze_algo(n):
    a,b,c = randomList(n)
    start_time = time()
    isIntersect_2(a, b, c)
    end_time = time() 
    elapsed = end_time - start_time 
    print("execution time:", elapsed)

def main():
    analyze_algo(100) #100 1000 10000 100000

main()
# def analyze_algo(n):
#     #stime = time()
#     a,b,c = randomList(n)
    #etime = time()
    #elapsed = etime - stime
    #print("create list time: ", elapsed)

    # print(n)

#     stime = time()
#     etime = time()
#     elapsed = etime - stime
#     print("execution time isintersect1: ", elapsed)

#     stime = time()
#     etime = time()
#     elapsed = etime - stime
#     print("execution time isintersect2: ", elapsed)

# analyze_algo(10000)
