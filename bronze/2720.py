T = int(input())

result=[]
for _ in range(T):
    C = int(input())
    Q = C // 25
    C %= 25
    D = C // 10
    C %= 10
    N = C // 5
    C %= 5
    P = C
    result.append([Q, D, N, P])
for i in result:
    print(*i)   