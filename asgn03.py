"""
----------------------------------------------------
asgn03.py
Assignment 3 functions.
----------------------------------------------------
Author: Qadeer Assan
ID: 160257370
Email: assa7370@mylaurier.ca
_updated_="2018-01-23"
----------------------------------------------------
"""
from stack_array import Stack

def stack_combine(s1, s2):
    """
    -------------------------------------------------------
    Combine the separate stacks into a doomon stack. Given stack is empty when
    function is done. Items are pushed alternately onto the returned stack.
    Order is not significant.
    Use: s3 = stack_combine(s1, s2)
    -------------------------------------------------------
    Preconditions:
        s1 - a stack to combine (Stack)
        s2 - another stack to combine(Stack)
    Postconditions:
        returns
        s3 - the values of s2 and s3 (Stack)
        s1 and s2 must be empty.
    -------------------------------------------------------
    """
    s3 = Stack()
    while s1.is_empty() != True or s2.is_empty() != True:
        if s1.is_empty() == False:
            s3.push(s1.pop())
        if s2.is_empty() == False:
            s3.push(s2.pop())
    return s3

def stack_split(s1):
    """
    -------------------------------------------------------
    Splits the given stack into separate stacks. Given stack is empty when
    function is done. Items are alternately pushed onto the returned stacks.
    Order is not significant.
    Use: s2, s3 = stack_split(s1)
    -------------------------------------------------------
    Preconditions:
        s1 - the stack to split into two parts (Stack)
    Postconditions:
        returns
        s2 - contains alternating values from given stack (Stack)
        s3 - contains other alternating values from given stack (Stack)
    -------------------------------------------------------
    """
    s2 = Stack()
    s3 = Stack()
    
    while s1.is_empty() != True:
        s2.push(s1.pop())
        if s1.is_empty() != True:
            s3.push(s1.pop())
        
    return s2, s3

IS_MIRROR = 0   # returned if string is a mirror
BAD_CHAR = 1    # returned if L or R contain characters not in v
NO_MIRROR = 2   # returned if string has no mirror string
MORE_LEFT = 3   # returned if too many characters in L
MORE_RIGHT = 4  # if too many characters in R
MISMATCHED = 5  # characters in L and R don't match

def mirror_stack(s, valid_chars, m):
    """
    -------------------------------------------------------
    Determines if string is a mirror of characters in valid_chars around the pivot m.
    A mirror is of the form LmR, where L is the reverse of R, and L and R
    contain only characters in valid_chars.
    Use: is_mirror = mirror_stack(string, valid_chars, m)
    -------------------------------------------------------
    Preconditions:
        string - a string (str)
        valid_chars - a string of valid characters (str)
        m - the mirror pivot string (str - one character not in valid_chars)
    Postconditions:
        returns
        is_mirror (int) - one of:
            IS_MIRROR - string is of the form LmR
            BAD_CHAR - L or R contains characters not in valid_chars
            NO_MIRROR - string does not contain m
            MORE_LEFT - too many characters in L
            MORE_RIGHT - too many characters in R
            MISMATCHED -  some characters in L and R don't match
    -------------------------------------------------------
    """
    stack = Stack()

    is_mirror = (len(s) == 0 or len(s) % 2 == 0)
    i = 0
    
    while is_mirror and i < len(s) and s[i] != m:
        if s[i] in valid_chars:
            stack.push(s[i])
            i+=1
        else:
            is_mirror = BAD_CHAR
        i +=1
    
    i +=1
    
    while is_mirror and i < len(s) and not stack.isempty():
        val = stack.pop()
        if val!= s[i]:
            is_mirror = MISMATCHED
        else:
            i+=1
    if not stack.is_empty():
        is_mirror = MORE_LEFT
    elif i < len(s) and stack.is_empty():
        is_mirror = MORE_RIGHT     
    
    return is_mirror