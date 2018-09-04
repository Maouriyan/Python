def descending(l):
    if len(l)<1:
        boo = True
    for i in range(0,len(l)-1):
        if l[i]>=l[i+1]:
            boo = True
        else :
            return False
    return boo
  
def valley(l):
    boo=False
    if len(l)<1:
        boo = True
    for i in range(0,len(l)-1):
        if l[i]>l[i+1]:
            continue
            
        else :
            if i<len(l)-1 and i>0:
                if l[i]<l[i+1]:
                    boo = True
                    continue
                else :
                    boo=False
        if not boo:
            return boo
    return boo

  

def transpose(m):
    n=[[m[j][i] for j in range(len(m))]for i in range(len(m[0]))]
    return n