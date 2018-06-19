#******************************************************************************
# parks.py
#******************************************************************************
# Name: 
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
#
# Distance on a sphere - The Haversine formula  - https://community.esri.com/groups/coordinate-reference-systems/blog/2017/10/05/haversine-formula
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
#
#
import math
#constants
central_park_latitude = 40.782800
central_park_longitude = -73.965269

prospect_park_latitude = 40.660217
prospect_park_longitude = -73.968948

flushing_park_latitude = 40.739694
flushing_park_longitude = -73.840793
    
def main():    
    input_user_is_good = False
    latitude = 0.0
    longitude = 0.0
    
    
    #input validaiton
    latitude = input ("Enter Latitude:")
    if validateUserInput(latitude) == True:
        longitude = input ("Enter Longitude:")    
        if validateUserInput(longitude) == True:
            input_user_is_good = True
                        
    #processing the input                    
    if input_user_is_good == True:
        latitude = float(latitude)
        longitude = float(longitude)
        
        #calculate the distances
        distance_central_park = calculateDistance(latitude,longitude,central_park_latitude, central_park_longitude)        
        distance_prospect_park = calculateDistance(latitude,longitude,prospect_park_latitude, prospect_park_longitude)        
        distance_flushing_park = calculateDistance(latitude,longitude,flushing_park_latitude, flushing_park_longitude)        
        
        #Print the lowest disance
        if distance_central_park < distance_prospect_park and distance_central_park < distance_flushing_park:
            print("Central Park is the closest park, with a distance of", distance_central_park , "km.")        
        elif distance_prospect_park < distance_central_park and distance_prospect_park < distance_flushing_park: 
            print("Prospect Park is the closest park, with a distance of", distance_prospect_park , "km.")        
        elif distance_flushing_park < distance_central_park and distance_flushing_park < distance_prospect_park: 
            print("Flushing Park is the closest park, with a distance of", distance_flushing_park , "km.")        
        
        print("\n\nWe can have a better approximation of this distance based on spherical geometry . Assuming that the radius of the earth is 6371 KM, we can conclude that: ")        
        #calculate the distances
        distance_central_park_sg = calculateDistanceInSphericalGeometry(latitude,longitude,central_park_latitude, central_park_longitude)        
        distance_prospect_park_sg = calculateDistanceInSphericalGeometry(latitude,longitude,prospect_park_latitude, prospect_park_longitude)        
        distance_flushing_park_sg = calculateDistanceInSphericalGeometry(latitude,longitude,flushing_park_latitude, flushing_park_longitude)        
        
        #Print the lowest disance
        if distance_central_park_sg < distance_prospect_park_sg and distance_central_park_sg < distance_flushing_park_sg:
            print("Central Park is the closest park, with a distance of", distance_central_park_sg , "km.")        
        elif distance_prospect_park_sg < distance_central_park_sg and distance_prospect_park_sg < distance_flushing_park_sg: 
            print("Prospect Park is the closest park, with a distance of", distance_prospect_park_sg , "km.")        
        elif distance_flushing_park_sg < distance_central_park_sg and distance_flushing_park_sg < distance_prospect_park_sg: 
            print("Flushing Park is the closest park, with a distance of", distance_flushing_park_sg , "km.")        
        
    else:
        print("bad input")    
    
def calculateDistance (loc1_latitude, loc1_longitude,loc2_latitude, loc2_longitude ):
    latitude_difference =  (111.048 *(loc1_latitude - loc2_latitude)) ** 2    
    longitude_difference =  (84.515 *(loc1_longitude - loc2_longitude)) ** 2    
    distance =  (latitude_difference + longitude_difference) ** (1/2)    
    return distance
def calculateDistanceInSphericalGeometry (loc1_latitude, loc1_longitude,loc2_latitude, loc2_longitude ):
    #elliptic riemannian geometry    
    phi_1 = math.radians(loc1_latitude)
    phi_2 = math.radians(loc2_latitude)

    delta_phi = math.radians(loc2_latitude - loc1_latitude)
    delta_lambda = math.radians(loc2_longitude - loc1_longitude)

    a = math.sin(delta_phi / 2.0) ** 2 + math.cos(phi_1) * math.cos(phi_2) * math.sin(delta_lambda / 2.0) ** 2
    
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    meters = 6371000 * c  
    km = meters / 1000.0  

    
    distance_km = km
    
    return distance_km
def calculateAbsoluteValue (x):
    if x < 0:
        return x * -1
    else:
        return x
def validateUserInput(value):
    #this function validates any value and guarantees that it could be converted to the type float
    #it also shows in the console what is wrong with the value if there is a problem
    #returns the same value
    try:
        float(value)                    
        return True
    except:
        print("The input needs to be numerical")
    return False

if __name__ == "__main__":
	main()

