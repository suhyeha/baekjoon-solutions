t=int(input())
results=[]
for _ in range(t):
    r,s=input().split()
    r=int(r)
    p=""
    for char in s:
        p+=char*r
    results.append(p)

for result in results:
    print(result)