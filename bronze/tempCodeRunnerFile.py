arr=[]
def push(k):
  return arr.append(k)

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
  
  while  N:
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

    N-=1
    if N==0:
      break
    
  return result

    
for x in stack():
  print(x)