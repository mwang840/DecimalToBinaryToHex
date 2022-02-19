from asyncio.windows_events import NULL
from string import digits
import unittest
import math


#Takes the binary of a number
def toBinary(number):
    remainder = ""
    remains = ""
    digit_ctr=0
    if(number < 0):
        return twosCompliment(number)

    while(number >= 1):
        if(number % 2 == 0):
            remainder += "0"
        elif(number % 2 == 1):
            remainder += "1"
        number = int(  math.floor(number / 2)  )
        digit_ctr+=1
    remains = remainder[::-1]
    return "0"*(32 - digit_ctr)  +remains

#turns a number to hex
def toHex(number):
    ctr = 0
    hexing = ""
    remainHexing = ""
    while(number >= 1):
        if(number % 16 == 10):
            hexing += "A"
        elif(number % 16 == 11):
            hexing += "B"
        elif(number % 16 == 12):
            hexing += "C"
        elif(number % 16 == 13):
            hexing += "D"
        elif(number % 16 == 14):
            hexing += "E"
        elif(number % 16 == 15):
            hexing += "F"
        else:
            hexing += str(number % 16)                        
        
        number = int(math.floor(number / 16))
        ctr += 1
        remainHexing = hexing[::-1]
    return "0" * (8-ctr) + remainHexing


##Takes the twos compliment of a number essientally flipping a bit
def twosCompliment(number):
    flipped_bit = ""
    remains = ""
    remainder = ""
    digit_ctr=0
    while(number <= -1):
        if(number % 2 == 0):
            remainder += "0"
        elif(number % 2 == 1):
            remainder += "1"
        number = int(math.ceil(number / 2))
        digit_ctr+=1
    remains = remainder[::-1]
    if(number % 2):
        flipped_bit += "1"
    else:
        flipped_bit += "0"
    flipped_bit = addsOne(flipped_bit)

    return flipped_bit

#adds One to a bit which will flip the bit by default
def addsOne(flipped_bit):
    reverse_bit = ""
    current_bit = flipped_bit
    for curr in current_bit:
        if (curr == "0"):
            reverse_bit += "1"
        else:
            reverse_bit += "0"
    return reverse_bit            

def splitToHex(binary):
    hex = binary
    codes = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    sums = 0
    for bin in binary:
        for non in enumerate(binary):
            if(sums == 10):
                hex += codes[sums - 1]
            elif(sums == 11):
                hex += codes[sums - 1]
            elif(sums == 12):
                hex += codes[sums - 1]  
            elif(sums == 13):
                hex += codes[sums - 1]
            elif(sums == 14):
                 hex += codes[sums - 1] 
            elif(sums == 15):
                hex += codes[sums - 1]                  
            else:
                hex += codes[sums - 1]


#Converts a hexidecimal back to a base ten number
def hexToDecimal(hex):
    baseTenNumber = 0
    multiple = 1
    ReverseHex = hex[::-1]
    for hexNum in ReverseHex:
        #If the letters are from A through F, multiple *= 10 up to 16
        if(hexNum == 'A'):
            #multiple *= 10
            baseTenNumber += (multiple * 10)
        elif(hexNum == 'B'):
            baseTenNumber += (multiple * 11)
        elif(hexNum == 'C'):
            baseTenNumber += (multiple * 12)
        elif(hexNum == 'D'):
            baseTenNumber += (multiple * 13)
        elif(hexNum == 'E'):
            baseTenNumber += (multiple * 14)
        elif(hexNum == 'F'):
            baseTenNumber += (15 * multiple)
        else:
            baseTenNumber += int(int(hexNum) * multiple)    
        multiple*=16                
                   
    return baseTenNumber

# Driver code
if __name__ == '__main__':
    input_ = 1
    print(toBinary(input_))
    print(toBinary(17))
    print(toBinary(20))
    print(hexToDecimal("16A"))
    print(toHex(256))
    print(addsOne("01100"))
    print(splitToHex("01111"))
   
