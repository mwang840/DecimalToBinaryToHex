from asyncio.windows_events import NULL
from string import digits
import unittest
import math
#Try using recursion




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

def toHex(number):
    ctr = 0
    hexing = ""
    
    while(number >= 1):
        if(number % 8 == 10):
            hexing = ""

    return "0" * (8-ctr) + hexing


##Takes the twos compliment of a number
def twosCompliment(number):
    flipped_bit = ""
    remains = ""
    digit_ctr=0
    if(number < 0):
        return twosCompliment(number)

    while(number <= -1):
        if(number % 2 == 0):
            remainder += "0"
        elif(number % 2 == 1):
            remainder += "1"
        number = int(  math.floor(number / 2)  )
        digit_ctr+=1
    remains = remainder[::-1]
    if(number % 2):
        flipped_bit += "1"
    else:
        flipped_bit += "0"
    flipped_bit = addOne(flipped_bit)

    return flipped_bit

#adds One to a bit
def addsOne(flipped_bit):
    flipped_bit += "1"

#Converts a hexidecimal back to a base ten number
def hexToDecimal(hex):
    baseTenNumber = 0
    multiple = 1
    ReverseHex = hex[::-1]
    for hexNum in ReverseHex:
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
    print(hexToDecimal("6A"))
