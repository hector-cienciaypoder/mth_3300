#******************************************************************************
# sprime.py
#******************************************************************************
# Name: Hector Valerio Lara Matias
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
#
#http://www.vogella.com/tutorials/JavaAlgorithmsPrimeFactorization/article.html
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

positive_integer = input("Please enter a positive integer:")
positive_integer = int(positive_integer)
factors_of_the_positive_integer = []
prime_factors_of_the_positive_integer = []


#Compute the integer factorization 
for n in range(1,positive_integer + 1):
    if (positive_integer % n) == 0:
        factors_of_the_positive_integer.append(n)

#compute the prime factorization
positive_integer_tmp = positive_integer
for n in range(2,positive_integer_tmp + 1):
    while ((positive_integer_tmp % n) == 0):        
        prime_factors_of_the_positive_integer.append(n)
        positive_integer_tmp = positive_integer_tmp / n        
        
print("The factors are", factors_of_the_positive_integer)        
print("The prime factors are", prime_factors_of_the_positive_integer)     



#criteria of being a sprime
is_sprime = False
has_either_three_or_four_factors = (len(factors_of_the_positive_integer) == 3 or len(factors_of_the_positive_integer) == 4)
is_equal_to_the_cube_of_one_the_factors = False
for factor in factors_of_the_positive_integer:
    if factor**3 == positive_integer:
        is_equal_to_the_cube_of_one_the_factors = True

     
if has_either_three_or_four_factors == True and is_equal_to_the_cube_of_one_the_factors == False:
    is_sprime = True

if is_sprime == True:
    print("Yes, this number is sprime")     
else:
    print("No, this number is not sprime")

