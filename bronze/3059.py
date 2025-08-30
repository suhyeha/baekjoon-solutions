T = int(input())

alpbat = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

fin = []

for i in range(T):
    word = input().strip()         
    use = set(word)                 
    miss = alpbat - use
    total = sum(ord(ch) for ch in miss)
    fin.append(str(total))         

print("\n".join(fin))        
