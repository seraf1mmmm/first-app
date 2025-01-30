class grand_father:
        speed = 100

class father(grand_father):
        height = 150

class son(father):
    pass

Antoha = grand_father
sun_Antohi = father
sun_sun_Antohi = son

print("Antoha's speed is " + str(Antoha.speed))
try:
    print("Antoha's height is " + str(Antoha.height))
except:
    print("Antoha don't have height")
print("Sun Antoha's speed is " + str(sun_Antohi.speed))
print("Sun Antoha's height is  " + str(sun_Antohi.height))


