"""
Create a function named divisors that takes an integer n > 1
returns an array with all the integer's divisors, except for 1 and the num itself
from smallest to largest.
If number is prime return the string '(integer) is prime'
"""

def divisors(integer):
    """
    This is a function to find all the multiples below a given integer that are
    % == 0.
    """
    divs = [n for n in range(2, integer, 1) if integer % n == 0] # creates a list from 2 to integer
    if divs == []: # if list is empty, no multiples for integer are % == 0 (excluding 1/integer itself)
        return f"{integer} is prime" # output will return integer identified as prime.
    else:
        return divs # returns a list of multiples for integer in range n>1 and n<integer



print(divisors(12)) # should return [2,3,4,6]

print(divisors(25)) # should return [5]

print(divisors(13)) # should return "13 is prime"

print(divisors(11)) # should return "11 is prime"

print(divisors(637)) # should return [7, 13, 49, 91]

print(divisors(17)) # should return "17 is prime"