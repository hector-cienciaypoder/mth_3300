#******************************************************************************
# trapezoid.py
#******************************************************************************
# Name: Hector Valerio Lara Matias.
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
#
#Romberg's method : https://en.wikipedia.org/wiki/Romberg%27s_method
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
    
    print("This program calculates the definite integral of sin (x^2) and cos(x^2) within the interval from a to b")
    
    a  = float(input("Please enter the start of the interval: "))
    b  = float(input("Please enter the end of the interval: "))
    n  = int(input("Please enter the steps: "))
    
    result = calculateSinX_TrapezoidMethod(a,b,n)
    print("(Trapezoid rule) the definite integral from",a,"to",b,"of the function sin(x^2) is", result)
    result = calculateCosX_TrapezoidMethod(a,b,n)
    print("(Trapezoid rule) the definite integral from",a,"to",b,"of the function cos(x^2) is", result)
    print("\n\n")
    result = calculateSinX_SimpsonMethod(a,b,n)
    print("(Simpson rule) the definite integral from",a,"to",b,"of the function sin(x^2) is", result)
    result = calculateCosX_SimpsonMethod(a,b,n)
    print("(Simpson rule) the definite integral from",a,"to",b,"of the function cos(x^2) is", result)
    print("\n\n")
#    result = calculateSinX_RombergMethod(a,b,n)
#    print("(Romberg rule) the definite integral from",a,"to",b,"of the function sin(x^2) is", result)
def calculateSinX_TrapezoidMethod(a,b,n):
    result = 0
        
    delta_x = (b-a)/n
    
    trapezoidal_first_factor = (b-a)/(2*n)
    #first term
    trapezoidal_second_factor = math.sin(a**2)
    #middle terms
    x = a + delta_x    
    for index in range(1,n):        
        f_x = math.sin(x**2)
        trapezoidal_second_factor = trapezoidal_second_factor + (2 * f_x)        
        x = x + delta_x
        
    #last term
    trapezoidal_second_factor = trapezoidal_second_factor + math.sin(b**2.0)    
    
    
    result = trapezoidal_first_factor * trapezoidal_second_factor
    return result
def calculateCosX_TrapezoidMethod(a,b,n):
    result = 0
    delta_x = (b-a)/n
    trapezoidal_first_factor = (b-a)/(2*n)
    #first term
    trapezoidal_second_factor = math.cos(a**2)
    #middle terms
    x = a + delta_x
    for index in range(1,n):
        trapezoidal_second_factor += 2 *(math.cos(x**2))
        x += delta_x
    #last term
    trapezoidal_second_factor += math.cos(b**2)    
    result = trapezoidal_first_factor * trapezoidal_second_factor
    return result
def calculateSinX_SimpsonMethod(a,b,n):
    result = 0
        
    delta_x = (b-a)/n
    
    trapezoidal_first_factor = (b-a)/(3*n)
    #first term
    trapezoidal_second_factor = math.sin(a**2)
    #middle terms
    x = a + delta_x    
    alternating_factor = 4
    for index in range(1,n):        
        f_x = math.sin(x**2)
        trapezoidal_second_factor += (alternating_factor * f_x)
        
        if alternating_factor == 4:
            alternating_factor = 2
        elif alternating_factor == 2:
            alternating_factor = 4
        x = x + delta_x
        
    #last term
    trapezoidal_second_factor += math.sin(b**2.0)    
    
    
    result = trapezoidal_first_factor * trapezoidal_second_factor
    return result
def calculateCosX_SimpsonMethod(a,b,n):
    result = 0
    delta_x = (b-a)/n
    trapezoidal_first_factor = (b-a)/(3*n)
    #first term
    trapezoidal_second_factor = math.cos(a**2)
    #middle terms
    x = a + delta_x
    alternating_factor = 4
    for index in range(1,n):
        trapezoidal_second_factor += alternating_factor *(math.cos(x**2))
        if alternating_factor == 4:
            alternating_factor = 2
        elif alternating_factor == 2:
            alternating_factor = 4
        x += delta_x
    #last term
    trapezoidal_second_factor += math.cos(b**2)    
    result = trapezoidal_first_factor * trapezoidal_second_factor
    return result

#pending could not do the Romberg method
#def function_h (a,b,n):    
#    print("function_h", n)
#    result = (b-a)/(2**n)
#    return result
#def function_r (n,m,a,b):
#    result = 0
#    if n == 0 and m == 0:
#        print("Start1", n, " ", m)
#        result = (b-a)/(2) * (math.sin(a**2) + math.sin(b**2))
#        print("end1",n, " ", m)
#    elif n > 0 and m == 0:
#        print("start2", n, " ", m)
#        first_value = function_r (n -1, 0 ,a,b)
#        H_n = (b-a)/(2**n)
#        print("start21",n, " ", m)
#        sum_of_the_series = 0
#        for k in range(1,2**(n - 1)):
#            sum_of_the_series += math.sin((a + (2*k - 1)*H_n )**2)
#            
#        result = (first_value/2.0) + (H_n * sum_of_the_series)        
#        print("end2",n, " ", m)
#    elif n > 0 and m > 0:
#        print("start1",n, " ", m)
#        first_value = function_r (n, m - 1,a,b)
#        second_value = function_r (n - 1, m - 1,a,b)
#        result = first_value + (first_value - second_value)/((4**m)- 1 )
#        print("end2",n, " ", m)
#    else:
#        print(n, " ", m)
#        result = 0
#    return result    
#def calculateSinX_RombergMethod(a,b,n):
#    if n < 5:
#        n = 6
#    print("romberg", n)        
#    result = function_r (n,0,a,b)        
#    print("romberg finished", n)        
#    return result
#def calculateCosX_RombergMethod(a,b,n):
#    result = 0
#    delta_x = (b-a)/n
#    trapezoidal_first_factor = (b-a)/(3*n)
#    #first term
#    trapezoidal_second_factor = math.cos(a**2)
#    #middle terms
#    x = a + delta_x
#    alternating_factor = 4
#    for index in range(1,n):
#        trapezoidal_second_factor += alternating_factor *(math.cos(x**2))
#        if alternating_factor == 4:
#            alternating_factor = 2
#        elif alternating_factor == 2:
#            alternating_factor = 4
#        x += delta_x
#    #last term
#    trapezoidal_second_factor += math.cos(b**2)    
#    result = trapezoidal_first_factor * trapezoidal_second_factor
#    return result
if __name__ == "__main__":
	main()