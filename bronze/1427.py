prime = [True]* 100001

prime[0]=prime[1]=False # 0,1은 소수가 아님

for i in range(2,1001):
    if prime[i]:
        for j in range(i*i,100001,i):
            prime[j]=False   #에라토스테네스의 체 핵심 코드
            

def special(N):
    if N+1 >100000 or not prime[N+1]:
        return False
    s=str(N)  #숫자를 문자열로 반환
    for i in range(1,len(s)):
        product = int(s[:i])*int(s[i:])+1
        if product > 100000 or not prime[product]:
            return False
    return True
# 누적합
cnt=[0]   #지금까지 소수인거 저장하는 리스트   현재 초기화상태
for i in range(1,100001):
    cnt.append(cnt[-1]+special(i))  # 개수세기
     # 이전 개수 +(이번에 하나 더 발견됐는지?)

#speical(i)= True 또는 False -> 1 or 0
#cnt[-1]=맨 마지막 값으로 지금까지 발견한 소수(speical)의 개수

T=int(input())
results = []  # 결과 저장용 리스트 추가
for _ in range(T):
    results.append(cnt[int(input())])  # 입력만 받고 결과 저장

# 모든 입력 다 받은 후에 출력
for result in results:
    print(result)
    
    
    

        