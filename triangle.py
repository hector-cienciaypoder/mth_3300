#******************************************************************************
# triangle.py
#******************************************************************************
# Name: 
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
#
# spherical law of cosines link: https://en.wikipedia.org/wiki/Spherical_law_of_cosines
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
#
#


# Copyright (C) 2018 Hector Valerio Lara Matias.
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
import math

def main():    
    input_user_is_good = False
    triangle_largest_side = 0.0
    triangle_middle_side = 0.0
    triangle_smallest_side = 0.0
    
    #input validaiton
    triangle_largest_side = input ("Enter largest side length:")
    if validateUserInput(triangle_largest_side) >= 0:
        triangle_middle_side = input ("Enter middle side length:")    
        if validateUserInput(triangle_middle_side) >= 0:
            triangle_smallest_side = input ("Enter smallest side length:")        
            if validateUserInput(triangle_smallest_side) >= 0:                                    
                if validateTriangleValues(triangle_largest_side,triangle_middle_side,triangle_smallest_side) >= 0:
                        input_user_is_good = True
                        
    #processing the input                    
    if input_user_is_good == True:
        print("The angles are:")
        triangle_largest_side = float(triangle_largest_side)
        triangle_middle_side = float(triangle_middle_side)
        triangle_smallest_side = float(triangle_smallest_side)
        
        #calculate the angle between the middle and the smallest side (it is always the largest)
        angle_largest = calculateAngleBetweenTwoSides(triangle_middle_side,triangle_smallest_side,triangle_largest_side)
        #calculate the angle between the largest and the smallest side
        angle_middle = calculateAngleBetweenTwoSides(triangle_largest_side,triangle_smallest_side,triangle_middle_side)                
        #calculate the angle between the largest and the middle side
        angle_smallest = calculateAngleBetweenTwoSides(triangle_largest_side,triangle_middle_side,triangle_smallest_side)
        
                     
        print(angle_largest)
        print(angle_middle)
        print(angle_smallest)
        
        more_info_ans = ""
        while 1:    
            more_info_ans = input("Do you want to see the angles within the logical system of Lobachevskian geometry(hyperbolic geometry) where the angle sum of a triangle is less than or equal to 180  and at most two parallel lines do exists for any given non-intersecting point and line?(y/n)")
            if more_info_ans == "y":
                angle_largest = calculateAngleBetweenTwoSidesLobachevskian(triangle_middle_side,triangle_smallest_side,triangle_largest_side)
                #calculate the angle between the largest and the smallest side
                angle_middle = calculateAngleBetweenTwoSidesLobachevskian(triangle_largest_side,triangle_smallest_side,triangle_middle_side)                
                #calculate the angle between the largest and the middle side
                angle_smallest = calculateAngleBetweenTwoSidesLobachevskian(triangle_largest_side,triangle_middle_side,triangle_smallest_side)
                
                             
                print(angle_largest)
                print(angle_middle)
                print(angle_smallest)
                
                
                break
            elif more_info_ans == "n":
            
                break
            else:
                print("Sorry bad input. Type y or n\n")
        
        more_info_ans2 = ""
        while 1:    
            more_info_ans2 = input("Do you want to see the angles within the logical system of double elliptic geometry(spherical geometry) where the angle sum of a triangle is greater than or equal to 180 and parallel lines do not exis?(y/n)")
            if more_info_ans2 == "y":
                angle_largest = calculateAngleBetweenTwoSidesElliptic(triangle_middle_side,triangle_smallest_side,triangle_largest_side)
                #calculate the angle between the largest and the smallest side
                angle_middle = calculateAngleBetweenTwoSidesElliptic(triangle_largest_side,triangle_smallest_side,triangle_middle_side)                
                #calculate the angle between the largest and the middle side
                angle_smallest = calculateAngleBetweenTwoSidesElliptic(triangle_largest_side,triangle_middle_side,triangle_smallest_side)
                
                             
                print(angle_largest)
                print(angle_middle)
                print(angle_smallest)
                
                
                break
            elif more_info_ans2 == "n":
            
                break
            else:
                print("Sorry bad input. Type y or n\n")
        
        
    else:
        print("bad input")    
    
def calculateAngleBetweenTwoSides (a,b,c):
    angle = math.acos(((a ** 2) + (b ** 2) - (c ** 2) )/(2*a*b)) #law of cosine
    angle = (angle * 180)/math.pi    #convert radians to degrees
    return angle
def calculateAngleBetweenTwoSidesLobachevskian (a,b,c):
    a = math.radians(a)
    b = math.radians(b)
    c = math.radians(c)
    angle = 0
    angle = math.acos((math.cos(c) - (math.cos(a)* math.cos(b)) )/(math.sin(a) * math.sin(b))) #law of cosine
    angle = (angle * 180)/math.pi    #convert radians to degrees
    return angle

def calculateAngleBetweenTwoSidesElliptic (a,b,c):
    #suppsing a gaussian curvature of -1 i.e. k = 1
    
    a = math.radians(a)
    b = math.radians(b)
    c = math.radians(c)
    num = (math.cosh(a) - (math.cosh(b)* math.cosh(c)) )
    den = (math.sinh(b) * math.sinh(c))
    angle = 0
    angle =  math.acos(num/den) #law of cosine
    angle = (angle * 180)/math.pi    #convert radians to degrees
    return angle
def validateTriangleValues(side1,side2,side3):
    #this function validates any value and guarantees that it could be converted to the type float
    #it also shows in the console what is wrong with the value if there is a problem
    #returns the same value
    side1 = float(side1)
    side2 = float(side2)
    side3 = float(side3)
    if not(side1 > side2 and side2 > side3):
        print ("The values of the sides of the triangle are not in descending order.  ")
        return -1
    elif not(  ((side1 + side2) >= side3) and ((side1 + side3) >= side2) and ((side2 + side3) >= side1)):
        print ("The values do not satisfy the triangle inequality theorem.")
        return -1
    return 1

def validateUserInput(value):
    #this function validates any value and guarantees that it could be converted to the type float
    #it also shows in the console what is wrong with the value if there is a problem
    #returns the same value
    try:
        value = float(value)            
        if value >= 0:
            return value
        else:
            print("The input needs to be positive")
    except:
        print("The input needs to be numerical")
    return -1


if __name__ == "__main__":
	main()