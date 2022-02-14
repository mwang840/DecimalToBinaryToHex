from string import digits

#Try using recursion
def toBinary(number):
    if(number >= 1):
        toBinary(number // 2)
    print(number % 2, end = '')    

#I will be using a while loop for this one
def toBinaryHex(number):
    remainder = ""
    remains = ""
    while(number >= 1):
        if(number % 2 == 0):
            remainder += "0"
        elif(number % 2 == 1):
            remainder += "1"
        number /= 2
    remains = remainder[::-1]
    toHex(number)   
    return remains            


def toHex(number):
    codes = ['0','1', '2','3','4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E']
    hexing = ''
    while(number !=0):
        modulous = number % 16
        if(modulous >=10):
            hexing += codes[modulous]
        number /= 16
    return hexing


import unittest

# Driver code
if __name__ == '__main__':
    print(toBinary(8))