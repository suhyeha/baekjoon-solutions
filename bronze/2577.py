a=int(input())
b=int(input())
c=int(input())
result=a*b*c
result_str=str(result)

count=[0]*10  

for ch in result_str:
    digit=int(ch)
    count[digit]+=1

for i in count:
    print(i)


