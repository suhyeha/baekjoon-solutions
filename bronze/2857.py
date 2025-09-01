members=[]
for i in range(5):
    member=input()
    members.append(member)

FBI_members=[] 
for i in range(5):
    if "FBI" in members[i]:
        FBI_members.append(i+1)
if FBI_members:
    print(*FBI_members)
else:
    print("HE GOT AWAY!")