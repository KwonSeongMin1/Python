a = "0111010"
answer = []

ans1=0
ans2=0
while(1):
    
    beforeLen=len(a)
    a = a.replace("0","")
    afterLen=len(a)
    s = format(afterLen,'b')
    ans1 = ans1 + 1
    ans2 = ans2 + (beforeLen - afterLen)
    
    if s == '1':
        break
    else:
        a = str(s)
    
print(beforeLen,afterLen)
    