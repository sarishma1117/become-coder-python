##number of even and odd in a list
def num_even_odd(n,data):
    even,odd=0,0
    for i in data:
        if i%2==0:
            even=even+1
        else:
            odd=odd+1
    return even,odd
            

n=int(input())
data=list(map(int,input().split()))
num=num_even_odd(n,data)
print(data)
print(*num)
