list=[0,1,3,4,6,7,9,10,12]
badpart=[]
def expand(b):
    badpart=[]
    l=list[len(list)-1]
    i=b
    if l==0:
        list.pop()
    else:
        k=len(list)-1
        list.pop()
        while list[k-1]!=l-1 and list[k-1]!=l-2:
            badpart.append(list[k-1])
            k-=1
        badpart.append(list[k-1])
        badpart.reverse()
        if l==list[len(list)-len(badpart)]+1:
             i=0
             while i<b:
                list.extend(badpart)
                i+=1
        else:
            diffs=[]
            p=len(badpart)-1
            s=0
            while s<=p:
                diffs.append(abs(badpart[s]-max(badpart[s-1],0)))
                s+=1
            i=0
            p=l-1
            diffs.insert(0,0)
            while i<b+2:
                s=0
                while s<len(diffs)-1:
                    list.append(i+p+diffs[s])
                    s+=1
                i+=1
b=3                
while len(list)>0:
  expand(b)
  b+=1
print(list)
