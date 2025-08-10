a=int(input())
b=int(input())
c=int(input())
result=a*b*c
result_str=str(result)

count=[0]*10  #0부터 9까지 카운트 저장 리스트

for ch in result_str:
    digit=int(ch)
    count[digit]+=1 #해당하는 숫자 카운트

for i in count:
    print(i)


#문자열로 변환해서 각 자리 숫자 카운트 하기

