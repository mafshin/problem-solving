# Distance from sun to planets in AU: Mercury:0.39 , Venus:0.72 , Earth:1.00 , Mars:1.52 , Jupiter:5.20, 
# Saturn:9.58 , Uranus:19.2 , Neptune:30.05 , Pluto:39.48
import math
distance={"Mercury" : 0.39 , "Venus" : 0.72 , "Earth" : 1.00 , "Mars" : 1.52 , "Jupiter" : 5.20,
"Saturn" : 9.58 , "Uranus" : 19.2 , "Neptune" : 30.05 , "Pluto" : 39.48}
dis=[]
for x in distance.values():
    x/=0.39
    dis.append(round(x))
dis.insert(0,0)
print(dis)
print("Sun",end="") 
i=0
for x in distance.keys():
    m=dis[i+1]-dis[i]
    for j in range(m):
      print("-",end="")
    print(x,end="")
    i+=1        
