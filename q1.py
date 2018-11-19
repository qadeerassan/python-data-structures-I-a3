"""
----------------------------------------------------
q1.py
Tests stack_combine.
----------------------------------------------------
Author: Qadeer Assan
ID: 160257370
Email: assa7370@mylaurier.ca
_updated_="2018-01-23"
----------------------------------------------------
"""
from stack_array import Stack
from asgn03 import stack_combine
s1 = Stack()
s2 = Stack()

s1.push(8)
s2.push(7)
s1.push(6)
s2.push(5)
s1.push(4)
s2.push(3)
s1.push(2)
s2.push(1)

s3 = stack_combine(s1, s2)
for i in s3:
    print(i)