T=input().strip().upper()

count={}

for chr in T:
    if chr in count:
        count[chr]+=1
    else:
        count[chr]=1
maximum_from_list=max(count, key=count.get)
if list(count.values()).count(count[maximum_from_list])>1:
    print("?")
else:
    print(maximum_from_list)


