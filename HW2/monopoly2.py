#******************************************************************************
# monopoly2.py
#******************************************************************************
# Name: Hector Valerio Lara Matias
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
#
#Python documentation - https://docs.python.org/2/library/functions.html#round
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


import random

def main():    
    number_of_simulations = 100000
    ending_in_trying_to_dismantle_pic = 0
    not_ending_in_trying_to_dismantle_pic = 0
    number_of_moves = 0
    for i in range(0,number_of_simulations):        
        roll1_number1 = random.randint(1,6)
        roll1_number2 = random.randint(1,6)
        #print("First roll:", roll1_number1, roll1_number2)
        if roll1_number1 != roll1_number2:
            #print("You move",roll1_number1 + roll1_number2 , "spaces")
            number_of_moves += (roll1_number1 + roll1_number2)
            continue
        
        roll2_number1 = random.randint(1,6)
        roll2_number2 = random.randint(1,6)
        #print("Second roll:", roll2_number1, roll2_number2)
        
        if roll2_number1 != roll2_number2:
            #print("You move",roll1_number1 + roll1_number2 + roll2_number1 + roll2_number2 , "spaces")
            number_of_moves += (roll1_number1 + roll1_number2 + roll2_number1 + roll2_number2)
            continue
            
        roll3_number1 = random.randint(1,6)
        roll3_number2 = random.randint(1,6)
        #print("Third roll:", roll3_number1, roll3_number2)
        
        if roll3_number1 != roll3_number2:
            #print("You move",roll1_number1 + roll1_number2 + roll2_number1 + roll2_number2 + roll3_number1 + roll3_number2 , "spaces")
            number_of_moves += (roll1_number1 + roll1_number2 + roll2_number1 + roll2_number2 + roll3_number1 + roll3_number2)
        else:
            #print("Go and dismantle the prison-industrial complex  ")
            ending_in_trying_to_dismantle_pic += 1
        
    not_ending_in_trying_to_dismantle_pic = number_of_simulations - ending_in_trying_to_dismantle_pic
    
    probability = ending_in_trying_to_dismantle_pic / number_of_simulations
    average_number_of_spaces = number_of_moves / not_ending_in_trying_to_dismantle_pic
    
    print("The probability that this game turn ends in the player going to dismantle the prison-industrial complex is ", probability, "which means",ending_in_trying_to_dismantle_pic,"out of",number_of_simulations,"or, in other words,",str(round(probability * 100.0,2)) + "%"  )
    print("\n\n")
    print("The estimate average amount of spaces moved per turn which does not end in trying to dismantle the prison-industrial complex is", average_number_of_spaces)
if __name__ == "__main__":
	main()