total = []
current = 0
for i in range(10):
    a, b = map(int, input().split())
    current = current - a + b 
    total.append(current)

print(max(total))



