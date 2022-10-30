import math
import matplotlib
import matplotlib.pyplot as plt
from math import pi
from math import atan 
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
# finding symmetry of ray vector of light with respect to the side of quadrilateral that the light hit 
#k+1 indicates line number
#symmetry of a vector with respect to b vector formula: [2*(a.b)/(|b|^2)]*b-a 
# t=2*(a.b) , m=|b|^2 
for i in range (1,11):
    print("i=",i)
    print("lenh=",lenh)
    print("widh=",widh)
    l=lenh[i]-lenh[i-1]
    w=widh[i]-widh[i-1]
    lengthv.append(l)
    widthv.append(w)
    print("lengthv=",lengthv)
    print("widthv=",widthv)
    t=2*(lengthv[3+i]*lengthv[k]+widthv[3+i]*widthv[k])
    m=lengthv[k]**2+widthv[k]**2
    t/=m                # t=2*(a.b)/(|b|^2)
    l=t*lengthv[k]-lengthv[3+i]  
    w=t*widthv[k]-widthv[3+i]
    print("l=",l,"    w=",w)
    if l!=0:
       slope=w/l
       print("slope=",slope)
       print("arctan(slope)=",(180/pi)*atan(slope) ," degrees")
    else:
       slope='infinity'
       print("slope=",slope)
       print("arctan(slope) =90 degrees")
    #formula of reflected ray line
    a.append(slope)
    print("a=",a)
    if a[4+i]!="infinity":  
       w=widh[i]-a[4+i]*lenh[i]
       b.append(w)
    else:
       b.append("parallel to Y-axis")
    #finding point of intersection
    #in order to find intersection point we should formula of 3 other sides of quadrilateral except that-
    #one which ray is reflected from, we have been on line k+1 until now so from i=1 till i=4 except i=k+1-
    # we should check line
    q=0
    for j in range (4):
        if j!=k:
            if a[j]=="infinity" and a[i+4]!="infinity":
                y=a[i+4]*lengths[j]+b[i+4]
                if (y-widths[j])*(y-widths[j+1])<0:
                    k=j
                    lenh.append(lengths[j])
                    widh.append(y)
                    q=1
            elif a[j]!="infinity" and a[i+4]=="infinity": 
                y=a[j]*lenh[i]+b[j]
                if  (y-widths[j])*(y-widths[j+1])<0:
                    k=j
                    lenh.append(lenh[i])
                    widh.append(y)
                    q=1  
            elif  a[j]!="infinity" and a[i+4]!="infinity": 
                x=(b[i+4]-b[j])/(a[j]-a[i+4])
                y=a[j]*x+b[j]
                if (x-lengths[j])*(x-lengths[j+1])<0:
                    k=j
                    lenh.append(x)
                    widh.append(y)
                    q=1 
           # else:  #side=="infinity" & ray=="infinity"                     
            #    print("ray and side are parallel")
        if q==1:
            break 
x=[]
y=[]               
for i in range (1,11):
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
                       