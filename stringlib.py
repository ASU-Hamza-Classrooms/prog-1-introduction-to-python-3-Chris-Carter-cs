#!/bin/python3

#I feel like I misunderstood the point of this assignment, but I'm not sure?

#Add the following functions:
#
#reverseStr - takes as input a string and returns the reverse of it
#
#containsWord - takes as input two strings, containingStr and containedStr,
#and returns "Yes" if containedStr is anywhere within containingStr 
#and returns "No" otherwise
#
#isPalindrome - takes as input a string and returns "Yes" if it is
#palindrome and "No" otherwise  
#
#upperCaseStr - takes as input a string and returns the identical string
#with the characters 'a' ... 'z' changed to uppercase
#

class stringlib:
    inputString = ""

    def __init__(self, inString):
        self.inputString = inString

#Add the following functions:
#
##reverseStr - takes as input a string and returns the reverse of it

    def reverseStr(self):
        return self.inputString[::-1]
    
##containsWord - takes as input two strings, containingStr and containedStr,
#and returns "Yes" if containedStr is anywhere within containingStr 
#and returns "No" otherwise

    def containsWord(self, target):
        if target in self.inputString:
            return "Yes"

        else:
            return "No"

##isPalindrome - takes as input a string and returns "Yes" if it is
#palindrome and "No" otherwise 

    def isPalindrome(self):
        if self.inputString == self.reverseStr:
            return "Yes"
        else:
            return "No"

##upperCaseStr - takes as input a string and returns the identical string
    def upperCaseStr(self):
        return self.inputString.upper()
