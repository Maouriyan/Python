def intreverse(n):
  a=0
  while(n>0): 
    
    a=(a*10)+(n%10)
    n=n//10
  return(a)

def matched(s):
    o=0
    for x in range(len(s)):
        if o>=0:
            
            if s[x]=="(":
                 o=o+1
            elif s[x]==")":
                 o=o-1
        else:
            return(False)
    if(o==0):
        return(True)
    else:
        return(False)
      
def isprime(l):
    if l>1:
        
        f=1
        for i in range (2,l):
                if l%i==0:
                    f=0
        if(f):
            return True
    else:
        return(False)
def sumprimes(l):
    sum=0
    for x in l:
        if isprime(x):
            sum=sum+x
                
    return(sum) 