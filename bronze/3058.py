T=int(input())
results=[]

for i in range(T):
    numbers=list(map(int,input().split()))
    evens = [num for num in numbers if num%2==0]
    results.append(f'{sum(evens)} {min(evens)}')

print("\n".join(results))
        
    


