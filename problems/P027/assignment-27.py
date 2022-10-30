txt=input("Enter a text:").split()
i=0
my_dict=[]
if txt[0]=="E:":
    print("Enter the dictionary:")
    while (1):
        x=input()
        if x=="END":
            break
        else:
          my_dict.append(x.split()) 
    for i in range(1,len(txt)):
        for j in range(len(my_dict)):
            if txt[i]==my_dict[j][0]:
               print(my_dict[j][1]," ",end="")
elif txt[0]=="P:":
    txt.pop(0)
    my_list=[chr(i) for i in range(97,122)]
    my_dict={}
    i=0
    for x in txt:
        my_dict[x]=my_list[i]
        i+=1   
    for x in txt:
       for y in my_dict.keys():
          if x==y:
            print(my_dict[y]," ",end="")
    print("\n")
    for x,y in my_dict.items():
        print(y,x)            
            






    