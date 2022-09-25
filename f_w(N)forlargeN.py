list=[9999999999999999999999999]
def knuth(n): #Defines a funcion
    m=list[len(list)-1]#m=last element
    if list[len(list) - 1]==0:#If last element is zero
        list.pop()#Remove last element
    else:#else
        i=n#i equals to function input
        list.pop()#Remove last element
        while i > 0:
            list.append(m-1)
            i-=1
            #Adds (last element-1) to list n times
m=3
while len(list) > 0:
    knuth(m)
    m=m+1
    # repeats until the list is empty with increasing m
print(m)#Prints HUGE number
