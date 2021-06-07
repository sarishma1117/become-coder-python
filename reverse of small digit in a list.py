##reverse of small digit in a list
def reverse(num):
    rev=0
    while num:
        r=num%10
        num=num//10
        rev=rev*10+r
    return rev

def findmin(n,data):
    s=min(data)
    print(s)
    r=reverse(s)            #max is same as this
    print(r)
    for i in range(n):
        if data[i]==s:
            data[i]=r
    s=min(data)
    print(data)
    return s==r


n=int(input())
data=list(map(int,input().split()))
minval=findmin(n,data)
print(minval)
