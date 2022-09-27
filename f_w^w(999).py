list=[[999]]
def expand(b):
    t=len(list)-1
    if list[t]==[]:
        list.pop()
    elif list[t][len(list[t])-1]==0:
        list[t].pop()
        k=list[t]
        i=0
        while i<=b:
            list.extend([k])
            i+=1
    else:
        k=list[t][len(list[t])-1]-1
        i=0
        list[t].pop()
        while i<=b:
            list[t].append(k)
            i+=1
b=3
while len(list)>0:
  expand(b)
  b+=1
print(b)
