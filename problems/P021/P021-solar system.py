solar_system = {"Mercury" : 58 , "Venus" : 120 , "Earth" : 180 , "Mars" : 250 , "Jupiter" : 777 , "Saturn" : 1430 , "Uranus" : 2880 , "Neptune" : 4500}
for a in solar_system :
    b = (int(solar_system[a] /58)) 
    print("sun" + b * "-" + a)