#uses string to unicode conversion for numbers
#check for integer overflow
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        negative = False
        number = 0
        str = str.strip()
        for i in range(len(str)):
            if str[i] == "-" and i == 0:
                negative = True
            elif str[i] == "+" and i == 0:
                continue
            elif (48 <= ord(str[i]) <= 57):
                number = number * 10 + int(str[i])
            else:
                break
                
        number = number if not negative else -number
        
        if number < -2**31:
            number = -2**31

        if number >= 2**31:
            number = 2**31 - 1

        return number
