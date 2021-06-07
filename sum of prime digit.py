

##sum of digits PRIME DIGITS
import math as m
def isprime(num):
    if num==1:
        return 0
    s=int(m.sqrt(num))
    for i in range(2,s+1):
        if num%i==0:
            return 0
    return 1
def findprimes(n,data):
    prime=[]
    nonprime=[]
    for i in data:            
        if isprime(i):
            prime.append(i)
        else:
            nonprime.append(i)
    return sum(prime),sum(nonprime)

n=int(input())
data=list(map(int,input().split()))
sumofdigits(n,data)
prime(*data)


