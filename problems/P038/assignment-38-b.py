import math
import matplotlib
import matplotlib.pyplot as plt
lengths=input("Enter 4 lengths of quadrilateral:").split()
widths=input("Enter 4 widths of quadrilateral :").split() 
for i in range (4):
    lengths[i]=int(lengths[i])
    widths[i]=int(widths[i])
lengths.append(lengths[0])
widths.append(widths[0])
print("lengths=",lengths)
print("widths=",widths)          
lenh=[]  #light source point's length and hit points's length
widh=[]  #light source point's width and hit point's width
x,y=input("Enter light source point's length and first hit point's length:").split()
lenh.append(int(x))
lenh.append(int(y))
x,y=input("Enter light source point's width and first hit point's width:").split()
widh.append(int(x))
widh.append(int(y))
a=[]     #slope of 4 sides of a quadrilateral and the line between light point and hit point to the side 
lengthv=[]   #length of sides's vector and first ray vector
widthv=[]    #width of sides's vector and first ray vector
for i in range (4):
    l=lengths[i+1]-lengths[i]
    w=widths[i+1]-widths[i]
    lengthv.append(l)
    widthv.append(w)   
    if l!=0:         #this is added cause i saw on i=4  can not calcuate w/l due to infinity slope 
        a.append(w/l)
    else:
        a.append("infinity")              
b=[]     #intercept of course about lines which their slope isn't infinity,if  so formula of line is x=b
for i in range(4):
    if a[i]!="infinity":
       w=widths[i]-a[i]*lengths[i]
       b.append(w)
    else:
        b.append("parallel to X-axis") 
a.append("not needed")
b.append("not needed")              
print("a=",a)
print("lengthv=",lengthv)
print("widthv=",widthv)        
print("b=",b)
# hit point test (we want to see hit point is on which side of quadrilateral)
i=0 
k=-1     
while k==-1:
    if a[i]!="infinity" :
        if widh[1]==a[i]*lenh[1]+b[i]:
            k=i
            print("hit point is on line",i+1)
        else:
            i+=1
    else:
        if lenh[1]==lengths[i] and (widh[1]-widths[i])*(widh[1]-widths[i+1])<0:
            k=i
            print("hit point is on line",i+1)
        else:
            i+=1
# slope of vertical lines to sides of quadrilateral  in order
av=[] 
for i in range (4):           
   if a[i]==0 :
    av.append("infinity")  
   elif a[i]=="infinity":
    t=0
    av.append(t)  
   else:
    t=-1/a[i]
    av.append(t)
print("av=",av)    
for i in range (10):
    print("i=",i)
    print("av[k]=",av[k]) 
    #intersection of  vertical line to side number k+1 in lenh[i+1] and parallel line with side number k+1 in lenh[i]
    if a[k]=="infinity":
        l=lenh[i]
        w=widh[i+1] 
    elif a[k]==0:
        l=lenh[i+1]
        w=widh[i]
    else:
        b1=widh[i]-a[k]*lenh[i]
        b2=widh[i+1]-av[k]*lenh[i+1]
        l=(b2-b1)/(a[k]-av[k])
        w=a[k]*l+b1   
    print("l=",l," w=",w)
    #distance between (1,w) and (lenh[i],widh[i])
    d=math.sqrt((l-lenh[i])**2+(w-widh[i])**2)
    print("d=",d)
    vi=(l-lenh[i])/d
    vj= (w-widh[i])/d
    print("vi=",vi,"   vj=",vj) 
    l=lenh[i]+vi*2*d
    w=widh[i]+vj*2*d
    print("symmetry of point=",l,w)
    #writing formula of reflected ray between point(l,w) and (lenl[i+1],widh[i+1])
    slope=(w-widh[i+1])/(l-lenh[i+1])
    a.append(slope)
    print("a=",a)
    t=widh[i+1]-a[i+5]*lenh[i+1]
    b.append(t)
    print("b=",b)
    q=0
    for j in range (4):
        if j!=k:
            if a[j]=="infinity" and a[i+5]!="infinity":
                y=a[i+5]*lengths[j]+b[i+5]
                if (y-widths[j])*(y-widths[j+1])<0:
                    k=j
                    lenh.append(lengths[j])
                    widh.append(y)
                    q=1
            elif a[j]!="infinity" and a[i+5]=="infinity": 
                y=a[j]*lenh[i+1]+b[j]
                if  (y-widths[j])*(y-widths[j+1])<0:
                    k=j
                    lenh.append(lenh[i+1])
                    widh.append(y)
                    q=1  
            elif  a[j]!="infinity" and a[i+5]!="infinity": 
                x=(b[i+5]-b[j])/(a[j]-a[i+5])
                y=a[j]*x+b[j]
                if (x-lengths[j])*(x-lengths[j+1])<0:
                    k=j
                    lenh.append(x)
                    widh.append(y)
                    q=1        
            print("q=",q)
            print("k=",k,"j=",j)
            print("lenh=",lenh)
            print("widh=",widh)         
           # else:  #side=="infinity" & ray=="infinity"                     
            #    print("ray and side are parallel")
        if q==1:
           break  
x=[]
y=[]               
for i in range (10):
    x.append(round(lenh[i],3))
    y.append(round(widh[i],3))
hit_points=list(zip(x,y))
print("hit_points=",hit_points) 
plt.plot(lengths,widths)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("quadrilateral")
plt.plot(lenh,widh)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Ray-tracing")
plt.show()                                             