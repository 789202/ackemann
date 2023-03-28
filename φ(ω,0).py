list=[0,1,999999999]
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
        while list[k-1]>=l:
            badpart.append(list[k-1])
            k-=1
        q=l-list[k-1]
        p=0
        s=1
        badpart.append(list[k-1])
        badpart.reverse()
        i=0
        while i<b:
            n=0
            s+=q-1
            while n<len(badpart):
                list.append(badpart[n]+s-1)
                n+=1
            i+=1
b=3
while len(list)>0:
    expand(b)
    b+=1
print(list)
