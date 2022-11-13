"""
Create a function named divisors that takes an integer n > 1
returns an array with all the integer's divisors, except for 1 and the num itself
from smallest to largest.
If number is prime return the string '(integer) is prime'
"""
from sympy import isprime  # import 'isprime' module to find prime number


def divisors(integer):
    """
    This is a function to find all the multiples below a given integer that are
    % == 0.
    """
    if isprime(integer): # if statement to identify if integer is a prime number.
        return f"{integer} is prime" # output will return integer identified as prime.
    else:
        divs = [n for n in range(2, integer, 1) if integer % n == 0]
        return divs # returns a list of multiples for integer in range n>1 and n<integer


print(divisors(12)) # should return [2,3,4,6]

print(divisors(25)) # should return [5]

print(divisors(13)) # should return "13 is prime"

print(divisors(11)) # should return "11 is prime"

print(divisors(637)) # should return [7, 13, 49, 91]

print(divisors(5)) # should return "5 is prime"