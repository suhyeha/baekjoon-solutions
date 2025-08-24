N=str(input())

count=0

for i in N:
    print(i, end='')
    count+=1
    
    if count%10==0:
        print()