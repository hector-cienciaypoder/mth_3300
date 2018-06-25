#******************************************************************************
# fence.py
#******************************************************************************
# Name: Hector Valerio Lara Matias.
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
#
#Python documentation - https://docs.python.org/3.0/library/turtle.html#turtle.setpos
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
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

import turtle



number_of_times = input("Please enter a positive integer greater than or equal to 2:")
number_of_times = int(number_of_times)

minimum_size = 25

#initialize

turtle.penup()
turtle.setx(10 + (turtle.window_width() * -1)/2)
turtle.sety(((turtle.window_height() )/2) - 10)
turtle.pendown()

for positive_integer in range(2,number_of_times + 1):
    #first part
    turtle.right(90)
    turtle.forward(minimum_size*3)
    
    #middle part
    for n in range(0,positive_integer - 2 ):
        turtle.left(90)
        turtle.forward(minimum_size)    
        turtle.left(90)
        turtle.forward(minimum_size*3)    
        turtle.left(180)
        turtle.forward(minimum_size*3)    
    #last part
    turtle.left(90)
    turtle.forward(minimum_size)    
    turtle.left(90)
    turtle.forward(minimum_size*3)    
    turtle.left(180)
    turtle.forward(minimum_size*2)    
    turtle.right(90)
    turtle.forward(minimum_size*(positive_integer-1))    
    turtle.left(90)
    turtle.penup()
    turtle.forward(minimum_size*2)
    turtle.pendown()
    turtle.left(90)
    
turtle.exitonclick()
        