import sys
input=sys.stdin.readline

arr=[]
def push(k):
  arr.append(k)

def pop():
  if not arr :
    return -1
  else:
    return arr.pop()
  
def size():
  return len(arr)

  
def empty():
  if not arr :
    return 1
  else:
    return 0
  
def top():
  if not arr:
    return -1
  else:
    return arr[-1]

def stack():
  N=int(input())
  result=[]
  
  for i in range(N):
    Q=input().split()
    
    if Q[0]=='push':
      push(int(Q[1]))
    
    elif Q[0]=='pop':
      result.append(pop())
    
    elif Q[0]=='size':
      result.append(size())
    
    elif Q[0] == 'empty':
      result.append(empty())
      
    elif Q[0] == 'top':
      result.append(top())
    
    
  return result

result=stack()
for x in result:
  print(x)