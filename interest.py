#******************************************************************************
# interest.py
#******************************************************************************
# Name: 
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
#
# "Aproximating Euler's Number correctly" - link: https://www.nayuki.io/page/approximating-eulers-number-correctly
# "How to check if a python module exists without importing it" - Stackoverflow - User: Yaberk - link: https://stackoverflow.com/questions/14050281/how-to-check-if-a-python-module-exists-without-importing-it#14050282
# "Main method in python - Stackoverflow" - link: https://stackoverflow.com/questions/8810765/main-method-in-python
#
# Reminder: you are to write your own code.
#
#
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
# Purpose: The purpose of this program is to calculate and output the continuous compound interest 
#          that is accumulated during the first 10 years of an investment that has a compounding frequency of 2 years
#
# Input: It requires from the user the following information in the exact order that is listed
#       (1) the initial principal of the investment (i.e. one integer or decimal number)
#       (2) five percent values that corresponds to the bi-annual periods 0-2, 2-4, 4-6, 6-8, 8-10 (i.e. four decimal numbers or integers)
#
# Output: The format of the output is the phrase "The final value is {final result}" 
#         where {final result} is the value of interest two decimal places
#
# Extraneous purpose: According to the specifications , "there is no penalty for showing additional values."
#                   Thus, the extraneous purpose is to show additional values
#                   The program will do the following after the specifications are met:
#                     (1) Ask the user whether he/she wants to see a comparison in terms of precision and time between Hector's method and other professional or unprofessional methods of doing the same calculation based on the numbers given by the user
#                     (2) If the user answers yes, show the comparison (the library mpmath will be considered the professional method)
#

# super simple design
# This program is divided into four small parts
#    the first part is responsible for calculating the account balance based on the function created by Hector Valerio Lara Matias
#    the second part is where the program begins and is responsible for calling the necessary functions based on the input of the user
#    The Third part is responsible for obtaining the information from the user and validating it
#    the fourth part uses the library mpmath to compare Hector's method with methods that are way more precise in handling the mathematical constant e 


#note : Anyone can add her or his function to the comparison list to discover the limits of computing in handling the mathematical constant e  

import time
import importlib
import fractions

mpmath_spec = importlib.util.find_spec("mpmath")
mpmath_found = mpmath_spec is not None
if mpmath_found == True:
    import mpmath
else:
    print("module mpmath was not found\n")


###########Third Part - Hector's method
#constants
compounding_frequency = 0.5
#my little research
#   I found out that
#   According to the python 3.6 documentation, "Floating point numbers are usually implemented using double in C"
#   According to wikipedia, on most systems the type double in C is defined by the IEEE 754 double-precision binary floating-point format (64 bits)
#   This means that floats use 64-bit of memory and it can hold up to 15 decimal places 
constant_e_with_15_decimals = 2.718281828459045  # this is the same constant as math.e
constant_e_with_2_decimals = 2.71 #one of the worst approximation of the constant e that can be found in this program. It can be 

##########################################################################
def compound_interest_fnc_hector (constant_e,initial_investment,percent1,percent2,percent3,percent4,percent5,compounding_frequency):    
    principal = initial_investment
    principal = principal * ((constant_e) ** (percent1 * compounding_frequency))
    principal = principal * ((constant_e) ** (percent2 * compounding_frequency))
    principal = principal * ((constant_e) ** (percent3 * compounding_frequency))
    principal = principal * ((constant_e) ** (percent4 * compounding_frequency))
    principal = principal * ((constant_e) ** (percent5 * compounding_frequency))               
    return principal
##########################################################################


###########First Part
def main():
    print("Welcome. This program calculates the continuous compound interest that is accumulated during the first 10 years of an investment that has a compounding frequency of 2 years\n")
    obtainUserInput()    
    if user_Input_Is_Valid == True:        
        print("\n")
        #run hector's method
        principal = compound_interest_fnc_hector(constant_e_with_15_decimals,initial_investment,percent1,percent2,percent3,percent4,percent5,compounding_frequency)
        #show values
        print("The final value is " + "$" + str(principal))
                
        
        
        
        #Extraneous purpose - additional values
        
        #Show comparison among different methods of doing the calculation based on user input
        more_info_ans = ""
        while 1:    
            more_info_ans = input("Do you want to see how the final value is calculated using more professional and unprofessional methods?(y/n)")
            if more_info_ans == "y":
                print("\n\n")
                #
                before_the_function = time.time()
                principal = compound_interest_fnc_hector(constant_e_with_15_decimals,initial_investment,percent1,percent2,percent3,percent4,percent5,compounding_frequency)
                after_the_function = time.time()
                
                
                print("**Hector's method with Constant e=2.718281828459045 (",after_the_function - before_the_function, "seconds) :\n", "The final value is\n" , "$" + str(principal), "\n")
                
                
                before_the_function = time.time()
                principal = compound_interest_fnc_hector(2.71,initial_investment,percent1,percent2,percent3,percent4,percent5,compounding_frequency)
                after_the_function = time.time()
                print("**Hector's method with Constant e=2.71 (",after_the_function - before_the_function, "seconds) :\n", "the final value is\n", "$" + str(principal), "\n")
                
                before_the_function = time.time()
                principal = compound_interest_fnc_hector(2.718,initial_investment,percent1,percent2,percent3,percent4,percent5,compounding_frequency)
                after_the_function = time.time()
                print("**Hector's method with Constant e=2.718 (",after_the_function - before_the_function, "seconds) :\n", "the final value is\n", "$" + str(principal), "\n")
                
                before_the_function = time.time()
                principal = compound_interest_fnc_hector(2.7182,initial_investment,percent1,percent2,percent3,percent4,percent5,compounding_frequency)
                after_the_function = time.time()
                print("**Hector's method with Constant e=2.7182 (",after_the_function - before_the_function, "seconds) :\n", "the final value is\n", "$" + str(principal), "\n")
                
                before_the_function = time.time()
                principal = compound_interest_fnc_hector(2.71828,initial_investment,percent1,percent2,percent3,percent4,percent5,compounding_frequency)
                after_the_function = time.time()
                print("**Hector's method with Constant e=2.71828 (",after_the_function - before_the_function, "seconds) :\n", "the final value is\n", "$" + str(principal), "\n")
                
                if mpmath_found == True:                    
                    #
                    before_the_function = time.time()
                    principal = compound_interest_fnc_mpmath_with_limit_definition_of_e(initial_investment,percent1,percent2,percent3,percent4,percent5,compounding_frequency)
                    after_the_function = time.time()
                    print("**mpmath - Limit definition (",after_the_function - before_the_function, "seconds) :\n", "the final value is\n", "$" + str(principal), "\n")
                    
                    #
                    before_the_function = time.time()
                    principal = compound_interest_fnc_mpmath_with_infinite_series_definition_of_e (initial_investment,percent1,percent2,percent3,percent4,percent5,compounding_frequency)
                    after_the_function = time.time()
                    print("**mpmath - Infinite series (",after_the_function - before_the_function, "seconds) :\n", "the final value is\n", "$" + str(principal), "\n")
            
                    before_the_function = time.time()
                    principal = compound_interest_fnc_mpmath_with_hyperbolic (initial_investment,percent1,percent2,percent3,percent4,percent5,compounding_frequency)
                    after_the_function = time.time()
                    print("**mpmath - Hyperbolic trigs (",after_the_function - before_the_function, "seconds) :\n", "the final value is\n", "$" + str(principal), "\n")
                
                before_the_function = time.time()
                principal = compound_interest_fnc_nayuki_precise_infinite_series (initial_investment,percent1,percent2,percent3,percent4,percent5,compounding_frequency)
                after_the_function = time.time()
                print("**Nayuki's precise method (",after_the_function - before_the_function, "seconds) :\n", "the final value is\n", "$" + str(principal), "\n")                
                #print(compute_exp(1, 10))
                
                before_the_function = time.time()
                principal = compound_interest_fnc_nayuki_imprecise_infinite_series (initial_investment,percent1,percent2,percent3,percent4,percent5,compounding_frequency)
                after_the_function = time.time()
                print("**Nayuki's imprecise method (",after_the_function - before_the_function, "seconds) :\n", "the final value is\n", "$" + str(principal), "\n")
                
                
                break
            elif more_info_ans == "n":
            
                break
            else:
                print("Sorry bad input. Type y or n\n")                        
###########Second Part
user_Input_Is_Valid = False
#user input variables
user_input_array = []
initial_investment = -1.0 
percent1 = -1.0
percent2 = -1.0
percent3 = -1.0
percent4 = -1.0
percent5 = -1.0

def validateUserInput(value):
    #this function validates any value and guarantees that it could be converted to the type float
    #it also shows in the console what is wrong with the value if there is a problem
    #returns the same value
    try:
        value = float(value)            
        if value >= 0:
            return value
        else:
            print("Sorry bad input. The input needs to be positive")
    except:
        print("Sorry bad input. The input needs to be numerical")
    return -1
def obtainUserInput():
    #this functions guarantees that the values given by the user are valid
    #it continues to ask user until it gets those values and then end    
    index = 0
    msg = "Enter the initial investment: "
    ordinals_array = ["first", "second", "third", "fourth", "fifth"]
    
    while index < 6:
        if index > 0:
            msg = "Enter the " +  ordinals_array[index - 1] + " interest rate (in percent): "
        user_input = input(msg)
        if validateUserInput(user_input) >= 0 :              
            user_input_array.append(user_input)
            index = index + 1
    global initial_investment,percent1,percent2,percent3,percent4,percent5,user_Input_Is_Valid
        
    initial_investment = float(user_input_array[0])        
    percent1 = float(user_input_array[1])/100.0
    percent2 = float(user_input_array[2])/100.0
    percent3 = float(user_input_array[3])/100.0
    percent4 = float(user_input_array[4])/100.0
    percent5 = float(user_input_array[5])/100.0
    user_Input_Is_Valid = True                                    
    return 1

    
###########Fourth Part - mpmath and Nayuki
#constants
constant_e_mpmath_limit_definition = 0 #this constant e is only used with hector's method
constant_e_mpmath_infinite_series_definition = 0 #this constant e is also only used with hector's method
if mpmath_found:
    mpmath.mp.dps = 100 #mpmath will use 100 decimal places numbers
    mpmath.mp.pretty = True
    constant_e_mpmath_limit_definition = mpmath.limit(lambda n: (1+1/n)**n, mpmath.inf)
    constant_e_mpmath_infinite_series_definition = mpmath.nsum(lambda n: 1/mpmath.fac(n), [0, mpmath.inf])




#this function will use a limit that is derived from putting(algebraically) the values of the compound interest formula inside of the limit definition of e 
#and then will evaluate the limit using mpmath with the hope that the result will be more precise. 
##########################################################################
def compound_interest_fnc_mpmath_with_limit_definition_of_e (initial_investment,percent1,percent2,percent3,percent4,percent5,compounding_frequency):            
    #converting the float values to numbers that have 100 decimal places
    initial_investment = mpmath.mpmathify(initial_investment)
    percent1 = mpmath.mpmathify(percent1)
    percent2 = mpmath.mpmathify(percent2)
    percent3 = mpmath.mpmathify(percent3)
    percent4 = mpmath.mpmathify(percent4)
    percent5 = mpmath.mpmathify(percent5)
    
    #   limit definition:  e^x = lim n->infinity (1+x/n)^n 
    principal = initial_investment
    x = percent1 * compounding_frequency
    principal = mpmath.limit(lambda n: ( principal * (1+(x/n))**n), mpmath.inf)
    x = percent2 * compounding_frequency
    principal = mpmath.limit(lambda n: (principal * (1+(x/n))**n), mpmath.inf)
    x = percent3 * compounding_frequency
    principal = mpmath.limit(lambda n: (principal * (1+(x/n))**n), mpmath.inf)
    x = percent4 * compounding_frequency
    principal = mpmath.limit(lambda n: (principal * (1+(x/n))**n), mpmath.inf)
    x = percent5 * compounding_frequency
    principal = mpmath.limit(lambda n: (principal * (1+(x/n))**n), mpmath.inf)        
    return principal
##########################################################################

#this function will use an infinite series that is derived from putting(algebraically) the values of the compound interest formula inside of the infinite series definition of e 
#and then will evaluate the infinite series using mpmath with the hope that the result will be more precise. 
def compound_interest_fnc_mpmath_with_infinite_series_definition_of_e (initial_investment,percent1,percent2,percent3,percent4,percent5,compounding_frequency):            
    #converting the float values to numbers that have 100 decimal places
    initial_investment = mpmath.mpmathify(initial_investment)
    percent1 = mpmath.mpmathify(percent1)
    percent2 = mpmath.mpmathify(percent2)
    percent3 = mpmath.mpmathify(percent3)
    percent4 = mpmath.mpmathify(percent4)
    percent5 = mpmath.mpmathify(percent5)
        
    #   infinite series definition:  e^x = inf(x^k/K!) taken from wikipedia    
    principal= initial_investment
    x = percent1 * compounding_frequency        
    principal =  mpmath.nsum(lambda n: principal * ((x**n)/mpmath.fac(n)), [0, mpmath.inf])
    x = percent2 * compounding_frequency
    principal =  mpmath.nsum(lambda n: principal * ((x**n)/mpmath.fac(n)), [0, mpmath.inf])
    x = percent3 * compounding_frequency
    principal =  mpmath.nsum(lambda n: principal * ((x**n)/mpmath.fac(n)), [0, mpmath.inf])
    x = percent4 * compounding_frequency
    principal =  mpmath.nsum(lambda n: principal * ((x**n)/mpmath.fac(n)), [0, mpmath.inf])
    x = percent5 * compounding_frequency
    principal =  mpmath.nsum(lambda n: principal * ((x**n)/mpmath.fac(n)), [0, mpmath.inf])    
    return principal
##########################################################################

##########################################################################
def compound_interest_fnc_mpmath_with_hyperbolic (initial_investment,percent1,percent2,percent3,percent4,percent5,compounding_frequency):            
    #converting the float values to numbers that have 100 decimal places
    initial_investment = mpmath.mpmathify(initial_investment)
    percent1 = mpmath.mpmathify(percent1)
    percent2 = mpmath.mpmathify(percent2)
    percent3 = mpmath.mpmathify(percent3)
    percent4 = mpmath.mpmathify(percent4)
    percent5 = mpmath.mpmathify(percent5)
    
    #   limit definition:  e^x = lim n->infinity (1+x/n)^n 
    principal = initial_investment
    x = percent1 * compounding_frequency    
    principal = principal * (mpmath.cosh(x) + mpmath.sinh(x))    
    x = percent2 * compounding_frequency
    principal = principal * (mpmath.cosh(x) + mpmath.sinh(x))
    x = percent3 * compounding_frequency
    principal = principal * (mpmath.cosh(x) + mpmath.sinh(x))
    x = percent4 * compounding_frequency
    principal = principal * (mpmath.cosh(x) + mpmath.sinh(x))
    x = percent5 * compounding_frequency
    principal = principal * (mpmath.cosh(x) + mpmath.sinh(x))    
    return principal
##########################################################################    

#The following functions are based on the ideas of Nayuki (a software developer graduated from the University of Canada)
#translated and modified by Hector Valerio Lara Matias
def nayuki_imprecise_infinite_series(principal, x):
    new_principal = 0.0
    factorial = 1.0    
    for n in range(0,99) :
        # When to terminate series?
        new_principal += principal * ((x**n) / factorial);  # How much error accumulated?
        factorial *= n + 1.0;    # Rounding error?                 
    return new_principal
def nayuki_precise_infinite_series(principal, x):    
    #print(float(compute_eulers_number( 18,x)))
    new_principal = principal * float(compute_eulers_number( 18,x))    
    return new_principal

def compound_interest_fnc_nayuki_imprecise_infinite_series(initial_investment,percent1,percent2,percent3,percent4,percent5,compounding_frequency):                
    principal = initial_investment
    x = percent1 * compounding_frequency        
    principal =  nayuki_imprecise_infinite_series(principal, x)
    x = percent2 * compounding_frequency
    principal =  nayuki_imprecise_infinite_series(principal, x)
    x = percent3 * compounding_frequency
    principal =  nayuki_imprecise_infinite_series(principal, x)
    x = percent4 * compounding_frequency
    principal =  nayuki_imprecise_infinite_series(principal, x)
    x = percent5 * compounding_frequency
    principal =  nayuki_imprecise_infinite_series(principal, x)            
    return principal

def compound_interest_fnc_nayuki_precise_infinite_series(initial_investment,percent1,percent2,percent3,percent4,percent5,compounding_frequency):                
    principal = initial_investment
    x = percent1 * compounding_frequency        
    principal =  nayuki_precise_infinite_series(principal, x)
    x = percent2 * compounding_frequency
    principal =  nayuki_precise_infinite_series(principal, x)
    x = percent3 * compounding_frequency
    principal =  nayuki_precise_infinite_series(principal, x)
    x = percent4 * compounding_frequency
    principal =  nayuki_precise_infinite_series(principal, x)
    x = percent5 * compounding_frequency
    principal =  nayuki_precise_infinite_series(principal, x)        
    return principal

# For example: compute_eulers_number(4) = "2.7183"
def compute_eulers_number(accuracy,x):
	if accuracy < 0:
		raise ValueError()
	
	sum = fractions.Fraction(0)
	factorial = 1.0      
	error_target = 10 ** accuracy
	scaler = fractions.Fraction(error_target)
	i = 0
	while True:
		term = fractions.Fraction(x**i/factorial)              
		sum += term     
        
      #factorial
		if i >= 1 and (factorial * (i+1)) > (x * error_target):  # i.e. term < 1/error_target         
			lower = round_fraction(sum * scaler) 
			upper = round_fraction((sum + term) * scaler)
			if lower == upper:
				# Note: The number of terms used is i+1
				s = str(lower)
				#print("term: ", s)
				return s[ : len(s) - accuracy] + "." + s[len(s) - accuracy : ]
		i += 1
		factorial *= i


HALF_FRACTION = fractions.Fraction(1, 2)

# Any rounding mode works correctly with compute_eulers_number().
# Round-half-to-even is implemented here, but truncation, flooring, etc. are acceptable too.
def round_fraction(num):
	result = num.numerator // num.denominator
	error = num - fractions.Fraction(result)
	if error > HALF_FRACTION or (error == HALF_FRACTION and result & 1 == 1):
		result += 1
	return result    

    
if __name__ == "__main__":
	main()
    
  