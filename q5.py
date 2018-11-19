"""
----------------------------------------------------
q5.py
Tests mirror_stack
----------------------------------------------------
Author: Qadeer Assan
ID: 160257370
Email: assa7370@mylaurier.ca
_updated_="2018-01-23"
----------------------------------------------------
"""
from asgn03 import mirror_stack
is_mirror = mirror_stack("cmc", "abc", "m")

results = ['IS_MIRROR','BAD_CHAR','NO_MIRROR','MORE_LEFT' ,'MORE_RIGHT','MISMATCHED']
print(results[is_mirror])

