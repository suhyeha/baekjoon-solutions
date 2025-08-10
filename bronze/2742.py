N=int(input())
list=[]
i=int(N)
for _ in range(N):
    list.append(i)
    i-=1
print(*list,sep='\n')