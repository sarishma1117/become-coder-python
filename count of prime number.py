import math as m
def isprime(num):
    s=int(m.sqrt(num))
    for i in range(2,s+1):
        if num%i==0:
            return 0
    return 1
    
def countprimes(n,data):
    pc=0
    for i in data:
        if isprime(i):
            pc=pc+1
    return isprime

n=int(input())
data=list(map(int,input().split()))
pc=countprimes(n,data)
print(pc)
