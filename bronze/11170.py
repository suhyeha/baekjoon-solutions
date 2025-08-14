T=int(input())
i=1
results=[]
for _ in range(T):
    a,b=map(int,input().split())
    count=sum(str(num).count("0") for num in range(a,b+1))
    results.append(count)
for i in results:
    print(i)