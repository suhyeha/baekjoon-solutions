a,b=map(int,input().split())

results=[]
num=1


while len(results)<=b:
    results+=[num]*num   #list 만들고 num만큼 반복
    num+=1

print(sum(results[a-1:b]))   #slice
