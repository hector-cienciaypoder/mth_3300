#******************************************************************************
# monopoly.py
#******************************************************************************
# Name: 
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
#
#
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
import random

def main():    
    roll1_number1 = random.randint(1,6)
    roll1_number2 = random.randint(1,6)
    print("First roll:", roll1_number1, roll1_number2)
    if roll1_number1 != roll1_number2:
        print("You move",roll1_number1 + roll1_number2 , "spaces")
        return 0
    
    roll2_number1 = random.randint(1,6)
    roll2_number2 = random.randint(1,6)
    print("Second roll:", roll2_number1, roll2_number2)
    
    if roll2_number1 != roll2_number2:
        print("You move",roll1_number1 + roll1_number2 + roll2_number1 + roll2_number2 , "spaces")
        return 0
        
    roll3_number1 = random.randint(1,6)
    roll3_number2 = random.randint(1,6)
    print("Third roll:", roll3_number1, roll3_number2)
    
    if roll3_number1 != roll3_number2:
        print("You move",roll1_number1 + roll1_number2 + roll2_number1 + roll2_number2 + roll3_number1 + roll3_number2 , "spaces")
    else:
        print("Go and dismantle the prison-industrial complex  ")
    
        
if __name__ == "__main__":
	main()