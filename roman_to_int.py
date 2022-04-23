"""
Problem:

Given a roman numeral, convert it to an integer.

Example 1:
Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

def romanToInt(s: str) -> int:
    """
    special cases:
    IV - 4, IX - 9
    XL - 40, XC - 90
    CD - 400, CM - 900
    
    general case:
    just one to one mapping of letter to number
    I: 1
    V: 5
    X: 10
    L: 50
    C: 100
    D: 500
    M: 1000
    
    The only real issue is how to handle special cases
    Straightforward solution, always check next, if next is bigger, then subtract current
    """
    # one to one mapping of letter to int
    romans = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    # the running total
    total = 0
    
    for index, letter in enumerate(s):
        # if this is not the last element (keeps us from index out of bounds)
        if index < len(s) - 1:
            # if next element is larger subtract, else add
            if romans[letter] < romans[s[index+1]]:
                total -= romans[letter]
            else:
                total += romans[letter]
        # this is the last element, just add it
        else:
            total += romans[letter]
    
    return total

"""
Complexity analysis:
Time: O(n) - we are just iterating over the string, but we are checking next so basically 2n
             but that's still O(n), since we have to touch every single value in the string O(n)
             is going to be our minimum

Space: O(n) - the only additional space we are using here is the romans dictionary and an 
              integer so still O(n)
"""