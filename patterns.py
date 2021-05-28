#10101
#01010
#10101
#01010
#10101
n=int(input())
for i in range(1,n+1):
    if i%2==0:
        for j in range(1,n+1):
            if j%2==0:
                j=1
            else:
                j=0
            print(j,end="")
        print()
    else:
        for j in range(1,n+1):
            if j%2==0:
                j=0
            else:
                j=1
            print(j,end="")
        print()

#10101
#10101
#10101
#10101
#10101
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if j%2==1:
            print("1",end="")
        else:
            print("0",end="")
    print()



#54321
#22222
#54321
#22222
#54321
n=int(input())
for i in range(1,n+1):
        for j in range(n,0,-1):
            if i%2==1:
                print(j,end="")
            if i%2==0:
                print(i,end="")
        print()



#12345
#22345
#32345
#42345
#52345
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==1:
            print(i,end=" ")
        else:
            print(j,end=" ")
    print()



#11111
#12345
#33333
#12345
#33333
n=int(input())
for i in range(1,n+1):
    if i%2:
        for j in range(1,n+1):
            print(i,end=" ")
    else:
        for j in range(1,n+1):
            print(j,end=" ")
    print()



#54321
#12345
#54321
#12345
#54321

n=int(input())
for i in range(1,n+1):
    if i%2==0:
        for j in range(n,0,-1):
            print(j,end=" ")
    else:
        for j in range(1,n+1):
            print(j,end=" ")
    print()





    
