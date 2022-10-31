def cal(n):
    i=1
    while i < len(n)-1:
      if n[i]=="*":
        k=n[i-1]*n[i+1]
        n.pop(i-1)
        n.pop(i-1)
        n.pop(i-1)
        n.insert(i-1,k)
        i-=1
      elif n[i]=="/":
        k=n[i-1]/n[i+1]
        n.pop(i-1)
        n.pop(i-1)
        n.pop(i-1)
        n.insert(i-1,k)
        i-=1
      elif n[i]=="%":
        k=n[i-1]%n[i+1]
        n.pop(i-1)
        n.pop(i-1)
        n.pop(i-1)
        n.insert(i-1,k)
        i-=1            
      i+=1
    print(n)
    i=1
    while i<len(n)-1: 
            
      if n[i]=="+":
        k=n[i-1]+n[i+1]
        n.pop(i-1)
        n.pop(i-1)
        n.pop(i-1)
        n.insert(i-1,k)
        i-=1
      elif n[i]=="-":
        k=n[i-1]-n[i+1]
        n.pop(i-1)
        n.pop(i-1)
        n.pop(i-1)
        n.insert(i-1,k)
        i-=1
      i+=1    
    print(n)
    m=n
    return m

answer=input("do you want to try with sample input?(y/n):")
if answer=="y":
  exp="3+(4+(5-2)*3)+7+(9-2*(7+(6-3)-2)+9)"
else:
  exp=input("Enter a numerical expresion:")
c=""
n=[]
j=0
for i in exp:
    print(i)
    if i.isdigit():
        c+=i
    else:
        if c:
          n.append(int(c))
          n.append(i)
          c=""
        else:
            n.append(i)  
if c:
  n.append(int(c))      
print(n)
open=[]
close=[]
i=0
while i<len(n):
  print(n)
  if n[i]=="(":
    open.append(i)
    print("open=",open,"i=",i)
  elif n[i]==")":
    close.append(i)
    print("close=",close,"i=",i)
    n[open[-1]:close[0]+1]=cal(n[open[-1]+1:close[0]])
    open.clear()
    close.clear()
    i=-1    
  i+=1
cal(n)
print(exp,"=",n[0])               