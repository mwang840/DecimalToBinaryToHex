from string import digits

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

import unittest

# Driver code
if __name__ == '__main__':
    print(toBinary(8))
