import sys
input=sys.stdin.readline

N=int(input())
A_WIN=0
B_WIN=0
for i in range(N):
    A,B=map(int, input().split())
    if A>B:
        A_WIN+=1
    elif A<B:
        B_WIN+=1
    else:
        pass
print(A_WIN,B_WIN)


    
    
    
