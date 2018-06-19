#******************************************************************************
# binary.py
#******************************************************************************
# Name: 
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
#
#Unicode table - https://unicode-table.com/en/
#ord function - https://docs.python.org/3/library/functions.html#ord
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
def main():
    #binary conversion part
    user_input_binary_str = input ("Enter an eight binary number:")
    
    decimal = convertToDecimal (user_input_binary_str)    
    #convertToDecimal returns -1 if the input is bad
    if decimal >= 0:        
        print("The binary number", user_input_binary_str,"is the same as the decimal number", str(decimal) + ".")
        
        #decimal conversion part
        user_input_decimal_str = input ("Now, enter a decimal integer between 0 and 255:")
        binary_str = convertToBinary (user_input_decimal_str)
        #convertToBinary returns an empty string if the input is bad
        if len(binary_str) > 0:
            print("This number is equivalent to the binary number", binary_str + ".")                            
        
def convertToDecimal(binary_str):
    #01010101
    validation = validateBinaryString(binary_str)
    if validation == True:        
        decimal_value = int(binary_str[0]) * (2**7)
        decimal_value += int(binary_str[1]) * (2**6)
        decimal_value += int(binary_str[2]) * (2**5)
        decimal_value += int(binary_str[3]) * (2**4)
        decimal_value += int(binary_str[4]) * (2**3)
        decimal_value += int(binary_str[5]) * (2**2)
        decimal_value += int(binary_str[6]) * (2**1)
        decimal_value += int(binary_str[7])                
        return decimal_value    
    else:
        return -1    
    
def convertToBinary(decimal_str):
    validation = validateDecimalString(decimal_str)
    if validation == True:                
        binary_str = ""    
        
        decimal = int(decimal_str)       
        if decimal == 0:
            return "00000000"                            
        binary_str = str(decimal % 2) + binary_str                        
        
        decimal = decimal // 2
        if decimal == 0:
            return "0000000" + binary_str
        binary_str = str(decimal % 2) + binary_str
        
        decimal = decimal // 2
        if decimal == 0:
            return "000000" + binary_str
        binary_str = str(decimal % 2)  + binary_str
        
        decimal = decimal // 2
        if decimal == 0:
            return "00000" + binary_str
        binary_str = str(decimal % 2)   + binary_str
  
        decimal = decimal // 2
        if decimal == 0:
            return "0000" + binary_str
        binary_str = str(decimal % 2)   + binary_str
      

        decimal = decimal // 2
        if decimal == 0:
            return "000" + binary_str
        binary_str = str(decimal % 2)   + binary_str
      

        decimal = decimal // 2
        if decimal == 0:
            return "00" +  binary_str
        binary_str = str(decimal % 2)   + binary_str
      

        decimal = decimal // 2
        if decimal == 0:
            return "0" + binary_str
        binary_str = str(decimal % 2)   + binary_str
                  
        #128
        
        return binary_str
    else:
        return ""

def validateBinaryString(value):
    #this function validates the input
    #it also shows in the console what is wrong with the value if there is a problem
    #returns true or false
    
    #check the length of the string
    if len(value) != 8:
        print("Sorry bad input. The binary number should have exactly eight digits")
    #check whether the string contains only zeroes and one
    elif (48 <= ord(value[0]) <= 49) and (48 <= ord(value[1]) <= 49) and (48 <= ord(value[2]) <= 49) and (48 <= ord(value[3]) <= 49) and (48 <= ord(value[4]) <= 49) and (48 <= ord(value[5]) <= 49) and (48 <= ord(value[6]) <= 49) and (48 <= ord(value[7]) <= 49):        
        #returns correct input
        return True
    else:
        print("Sorry bad input. The binary number should contain only zeroes and one")
    #returns bad input
    return False

def validateDecimalString(value):
    #this function validates the input
    #it also shows in the console what is wrong with the value if there is a problem
    #returns true or false
    
    #check the length of the string
    length = len(value)
    if 1 <= length <= 3:
        
        #check whether is the string contains only numerical values
        only_numerical = True
        
        if length >= 1:
            if not (48 <= ord(value[0]) <= 57):
                only_numerical = False        
        
        if length >= 2:
            if not (48 <= ord(value[1]) <= 57):
                only_numerical = False        
        
        if length >= 3:
            if not (48 <= ord(value[2]) <= 57):
                only_numerical = False                
        
        if only_numerical:
            #returns correct input
            return True                
        else:
            print("Sorry bad input. The decimal number should contain only numerical values")                    
    #check whether the string contains only numerical values
    else:        
        print("Sorry bad input. The decimal number should be between 0 and 255")                
    
    #returns bad input
    return False



if __name__ == "__main__":
	main()