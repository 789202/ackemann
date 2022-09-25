list=[0,1,2,3,4,5,6,7,8,9]
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
        while list[k-1]!=l-1:
            badpart.append(list[k-1])
            k-=1
        badpart.append(list[k-1])
        badpart.reverse()
        i=0
        while i<b:
            list.extend(badpart)
            i+=1
b=3
while len(list)>0:
    expand(b)
    b+=1
print(b)
