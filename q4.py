"""
----------------------------------------------------
q4.py
Tests split()
----------------------------------------------------
Author: Qadeer Assan
ID: 160257370
Email: assa7370@mylaurier.ca
_updated_="2018-01-23"
----------------------------------------------------
"""
from stack_array import Stack

s1 = Stack()

s1.push(1)
s1.push(5)
s1.push(7)
s1.push(8)
s1.push(9)
s1.push(12)
s1.push(14)
s1.push(8)
s1.push(999)

s2, s3 = s1.split()
print("***s2")
for i in s2:
    print(i)
print("***s3")
for j in s3:
    print(j)
