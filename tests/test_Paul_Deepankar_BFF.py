
"""
As a user
So that I can find my tasks among all my notes
I want to check if a line from my notes includes the string `#TODO`.

"""

from lib.Paul_Deepankar_BFF import *

def test_the_begining():
    assert includes_todo("#TODO Buy Milk") == True


def test_in_the_middle():
    assert includes_todo("Remeber to submit #TODO the assignment") == True

def test_at_the_end():
    assert includes_todo("Go to gym #TODO") == True

def test_no_present():
    assert includes_todo("Drink tea") == False

def test_empty_string():
    assert includes_todo(" ") == False

def test_lower_case():
    assert includes_todo("#todo have a shower!") == False