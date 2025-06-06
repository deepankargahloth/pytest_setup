
from lib.fizzbuzz import *

"""
Given a number not divisible by 3 or 5 (e.g. 1)
it return that number
"""
def test_given_non_3_5_divisible_return_number():
    result = fizzbuzz(1)
    assert result == 1