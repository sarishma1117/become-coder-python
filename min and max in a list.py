






##min and max in a list
def minandmax(n,data):
    max=0
    min=9
    c1=0
    c2=0
    for i in data:
        r=n%10
        n=n//10
        if r>max:
            max=r
            c1=1
        elif max==r:
            c1+=1
        if r<min:
            min=r
            c2=1
         elif min==r:
             c2+=1
    return min,max

n=int(input())
data=list(map(int,input().split()))
mi,ma=minandmax(n,data)
print(mi,ma)
print(c1,c2)


