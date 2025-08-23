a,b=map(int, input().split())

reverse_number1=int(str(a)[::-1])
reverse_number2=int(str(b)[::-1])

print(max(reverse_number1,reverse_number2))